

USE bancoPython
GO


CREATE OR ALTER PROCEDURE P_cadastroCliente
    @uf CHAR(2),
    @cidade VARCHAR(50),
    @logradouro VARCHAR(100),
    @cep CHAR(9),
    @bairro VARCHAR(100),
    @nome VARCHAR(50),
    @cpf CHAR(11),
    @email VARCHAR(100),
    @senha VARCHAR(255),
    @data_nascimento DATE,
    @numero_residencia VARCHAR(50),
    @complemento VARCHAR(50),
    @telefone CHAR(11),
    @tipo VARCHAR(50)
AS
BEGIN
    DECLARE @id_uf INT
    DECLARE @id_cidade INT
    DECLARE @id_endereco INT
    DECLARE @id_usuario INT

    BEGIN TRY
        BEGIN TRANSACTION
            -- ve se o email existe
            IF EXISTS (SELECT 1 FROM tbl_usuario WHERE email = @email)
                THROW 50001, 'EMAIL JA ESTA CADASTRADO', 1;
            -- ve se o cpf existe
            IF EXISTS (SELECT 1 FROM tbl_usuario WHERE cpf = @cpf)
                THROW 50002, 'CPF JA ESTA CADASTRADO', 1;
            -- ve se o uf  existe na tabela uf 
            SET @id_uf = (SELECT id_uf FROM tbl_uf WHERE uf = @uf)
            IF @id_uf IS NULL
                THROW 50003, 'UF NAO ENCONTRADO', 1;

            SET @id_cidade = (SELECT id_cidade FROM tbl_cidade WHERE cidade = @cidade AND id_uf_fk = @id_uf)
            IF @id_cidade IS NULL
            BEGIN
                INSERT INTO tbl_cidade (cidade, id_uf_fk) VALUES (@cidade, @id_uf)
                SET @id_cidade = SCOPE_IDENTITY()
            END

            -- insere na endereço
            INSERT INTO tbl_endereco (logradouro, cep, bairro, status_endereco, id_cidadeFK)
            VALUES (@logradouro, @cep, @bairro, 'ATIVO', @id_cidade)
            SET @id_endereco = SCOPE_IDENTITY()

            -- insere na usuario
            INSERT INTO tbl_usuario (nome_usuario, cpf, email, senha, data_nascimento, numero_residencia, complemento, id_endereco_fk)
            VALUES (@nome, @cpf, @email, @senha, @data_nascimento, @numero_residencia, @complemento, @id_endereco)
            SET @id_usuario = SCOPE_IDENTITY()

            -- insere na telefone
            INSERT INTO tbl_telefone (telefone, tipo, status_telefone, id_usuario_fk)
            VALUES (@telefone, @tipo, 'ATIVO', @id_usuario)

            -- insere na cleinte
            INSERT INTO tbl_cliente (data_cadastro, status_cliente, id_usuario_fk)
            VALUES (CAST(GETDATE() AS DATE), 'ativo', @id_usuario)

        COMMIT
        PRINT 'Cliente cadastrado com sucesso'

    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK
        PRINT 'Erro: ' + ERROR_MESSAGE()
    END CATCH
END
GO
--=================================================================================================



CREATE OR ALTER PROCEDURE P_BuscarClientePorNome
    @nome VARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;
    SELECT 
        c.id_cliente,
        u.nome_usuario,
        u.cpf,
        u.email,
        u.data_nascimento,
        c.data_cadastro,
        c.status_cliente
    FROM tbl_usuario u
    INNER JOIN tbl_cliente c
        ON u.id_usuario = c.id_usuario_fk
    WHERE u.nome_usuario LIKE '%' + @nome + '%';
END
GO

EXEC P_BuscarClientePorNome 'João Teste';
GO
--=================================================================================================

CREATE OR ALTER PROCEDURE P_BuscarClienteEmail
    @email VARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;
    SELECT
        c.id_cliente,
        u.nome_usuario,
        u.cpf,
        u.email,
        u.data_nascimento,
        c.data_cadastro,
        c.status_cliente
    FROM tbl_usuario u 
    INNER JOIN tbl_cliente c
        ON u.id_usuario = c.id_usuario_fk
    WHERE u.email LIKE '%' + @email + '%';
END
GO

EXEC P_BuscarClienteEmail 'aaaaaaa';
GO
--=================================================================================================

CREATE OR ALTER PROCEDURE P_BuscarClientes
AS
BEGIN
    SET NOCOUNT ON;
    SELECT
        c.id_cliente,
        u.nome_usuario,
        u.cpf,
        u.email,
        u.data_nascimento,
        c.data_cadastro,
        c.status_cliente
    FROM tbl_usuario u 
    INNER JOIN tbl_cliente c
        ON u.id_usuario = c.id_usuario_fk
END
GO

EXEC P_BuscarClientes; 
GO
--=================================================================================================

CREATE OR ALTER PROCEDURE P_BuscarClienteCpf
    @cpf CHAR(11) 
AS
BEGIN
    SET NOCOUNT ON;
    SELECT
        c.id_cliente,
        u.nome_usuario,
        u.cpf,
        u.email,
        u.data_nascimento,
        c.data_cadastro,
        c.status_cliente
    FROM tbl_usuario u 
    INNER JOIN tbl_cliente c
        ON u.id_usuario = c.id_usuario_fk
    WHERE u.cpf = @cpf;
END
GO

EXEC P_BuscarClienteCpf  '12345678001';
GO

--=================================================================================================

CREATE OR ALTER PROCEDURE P_BuscarClientDataNasc
    @data_nascimento DATE
AS
BEGIN
    SET NOCOUNT ON;


    SELECT
        c.id_cliente,
        u.nome_usuario,
        u.cpf,
        u.email,
        u.data_nascimento,
        c.data_cadastro,
        c.status_cliente
    FROM tbl_usuario u 
    INNER JOIN tbl_cliente c
        ON u.id_usuario = c.id_usuario_fk
    WHERE u.data_nascimento = @data_nascimento;
END
GO

EXEC P_BuscarClientDataNasc  '2000-01-01';
GO
--=================================================================================================

CREATE OR ALTER PROCEDURE P_atualizar_estatusbloqueado
    @id_cliente INT,
    @status_cliente VARCHAR(100)  
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT EXISTS(SELECT 1 FROM tbl_cliente WHERE id_cliente = @id_cliente)
        THROW 50001,'CLIENTE NAO ENCONTRADO' ,1;

    IF (
        SELECT COUNT(*) 
        FROM tbl_emprestimo 
        WHERE id_clientefk = @id_cliente 
        AND status_emprestimo = 'atrasado'
    ) >= 4
    BEGIN
        BEGIN TRY
            BEGIN TRANSACTION;

                UPDATE tbl_cliente
                SET status_cliente = @status_cliente
                WHERE id_cliente = @id_cliente;

                PRINT 'ATUALIZADO COM SUCESSO'

            COMMIT;
        END TRY
        BEGIN CATCH
            ROLLBACK;
            THROW; 
        END CATCH
    END
    ELSE
        THROW 50005, 'Cliente nao possui emprestimos suficientes para ser bloqueado', 1;
END
GO
--=================================================================================================
--ela verifica se nao existe um cliente com id informado e ele estiver ativo informa 
--se o email for igual a antiga nao pode atualizar e se nao ela atualiza
CREATE OR ALTER PROCEDURE P_atualizarEmail
    @id_usuario INT,
    @email VARCHAR(100),
    @senha VARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT EXISTS (
        SELECT 1
        FROM tbl_usuario u
        INNER JOIN tbl_cliente c ON u.id_usuario = c.id_usuario_fk
        WHERE u.id_usuario = @id_usuario 
        AND c.status_cliente = 'ativo'
    )
        THROW 50002, 'Cliente nao encontrado ou bloqueado', 1;

IF EXISTS (
    SELECT 1
    FROM tbl_usuario
    WHERE id_usuario = @id_usuario
    AND email = @email
)
    THROW 50001, 'EMAIL NAO PODE SER IGUAL AO ANTERIOR', 1;

IF EXISTS (
    SELECT 1
    FROM tbl_usuario
    WHERE email = @email
    AND id_usuario <> @id_usuario
)
    THROW 50002, 'EMAIL JA CADASTRADO', 1;

    BEGIN TRY
        BEGIN TRANSACTION
            UPDATE tbl_usuario 
            SET email = @email,
                senha = @senha
            WHERE id_usuario = @id_usuario;
        COMMIT;
    END TRY
    BEGIN CATCH
        ROLLBACK;
        THROW; 
    END CATCH
END
GO
--=================================================================================================
--ela verifica se nao existe um cliente com id informado e ele estiver ativo informa 
--se a senha for igual a antiga nao pode atualizar e se nao ela atualiza
CREATE OR ALTER PROCEDURE P_atualizarSenha
    @id_usuario INT,
    @senha VARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;


    IF NOT EXISTS (
        SELECT 1
        FROM tbl_usuario u
        INNER JOIN tbl_cliente c ON u.id_usuario = c.id_usuario_fk
        WHERE u.id_usuario = @id_usuario 
        AND c.status_cliente = 'ativo'
    )
        THROW 50002, 'Cliente nao encontrado ou bloqueado', 1;

    IF EXISTS (SELECT 1 FROM tbl_usuario WHERE id_usuario = @id_usuario AND senha = @senha)
        THROW 50001, 'SENHA NAO PODE SER IGUAL A ANTERIOR', 1;

    BEGIN TRY
        BEGIN TRANSACTION
            UPDATE tbl_usuario 
            SET senha = @senha
            WHERE id_usuario = @id_usuario;
        COMMIT;
    END TRY
    BEGIN CATCH
        ROLLBACK;
        THROW; 
    END CATCH
END
GO
--=================================================================================================

CREATE OR ALTER PROCEDURE P_ExcluirCliente 
    @id_cliente INT
AS
BEGIN
    SET NOCOUNT ON;
    -- ve se o cliente existe
    IF NOT EXISTS (SELECT 1 FROM tbl_cliente WHERE id_cliente = @id_cliente)
        THROW 50002, 'CLIENTE NAO ENCONTRADO', 1;
    -- ve se tem emprestimo
    IF EXISTS (SELECT 1 FROM tbl_emprestimo WHERE id_clientefk = @id_cliente)
        THROW 50001, 'CLIENTE NAO PODE SER EXCLUIDO POIS POSSUI EMPRESTIMOS', 1;

    BEGIN TRY
        BEGIN TRANSACTION
            DELETE FROM tbl_cliente
            WHERE id_cliente = @id_cliente;
        COMMIT
    END TRY
    BEGIN CATCH
        ROLLBACK;
        THROW;
    END CATCH
END
GO
--=================================================================================================

--so desativa o endereço nao exclui
--vc sempre deleta a filha primeiro pra depois a filha 
CREATE OR ALTER TRIGGER TR_ExcluirCliente
ON tbl_cliente
AFTER DELETE 
AS 
BEGIN
    SET NOCOUNT ON;

    BEGIN TRAN
    BEGIN TRY

        
        DECLARE @id_usuario INT
        DECLARE @id_endereco INT

        SELECT @id_usuario = id_usuario_fk FROM DELETED -- varfiavel q vai receber o valor deletado pra deletar na usuario
        SELECT @id_endereco = id_endereco_fk FROM tbl_usuario WHERE id_usuario = @id_usuario -- variavel recebe o valor do endereço pra desat6ivar

        
        DELETE FROM tbl_telefone WHERE id_usuario_fk = @id_usuario

        
        DELETE FROM tbl_usuario WHERE id_usuario = @id_usuario

       
        UPDATE tbl_endereco 
        SET status_endereco = 'INATIVO'
        WHERE id_endereco = @id_endereco

        COMMIT
    END TRY
    BEGIN CATCH
        ROLLBACK;
        THROW;
    END CATCH
END
GO





SELECT * FROM tbl_uf;
SELECT * FROM tbl_cidade;
SELECT * FROM tbl_endereco;
SELECT * FROM tbl_livro;
SELECT * FROM tbl_usuario;
SELECT * FROM tbl_cliente;
SELECT * FROM tbl_funcionario;
SELECT * FROM tbl_telefone;
SELECT * FROM tbl_emprestimo;


