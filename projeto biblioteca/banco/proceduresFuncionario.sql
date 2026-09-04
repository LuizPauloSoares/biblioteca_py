USE bancoPython
GO



CREATE OR ALTER PROCEDURE P_buscarFuncionario
    @id_matricula INT 
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT EXISTS (SELECT 1 FROM tbl_funcionario WHERE id_matricula = @id_matricula)
    THROW 50001,'FUNCIONARIO NAO ENCONTRADO',1;

    SELECT 
        u.nome_usuario,
        u.cpf,
        u.email,
        FORMAT(u.data_nascimento, 'dd/MM/yyyy') AS data_nascimento,
        f.id_matricula,
        f.cargo,
        f.salario
    FROM tbl_usuario u
    INNER JOIN tbl_funcionario f
        ON u.id_usuario = f.id_usuario_fk  
    WHERE f.id_matricula = @id_matricula; 
END
GO
--=================================================================================================
CREATE OR ALTER PROCEDURE P_buscarFuncionarios
AS
BEGIN
    SET NOCOUNT ON;
    SELECT
        u.nome_usuario,
        u.cpf,
        u.email,
        FORMAT(u.data_nascimento, 'dd/MM/yyyy') AS data_nascimento,
        f.id_matricula,
        f.cargo
    FROM tbl_usuario u
    INNER JOIN tbl_funcionario f
        ON u.id_usuario = f.id_usuario_fk  
END
GO
--=================================================================================================
CREATE OR ALTER PROCEDURE P_BuscarFuncionarioPorNome
    @nome VARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON; 
    SELECT          
        u.nome_usuario,
        u.cpf,
        u.email,
        FORMAT(u.data_nascimento, 'dd/MM/yyyy') AS data_nascimento,
        f.id_matricula,
        f.cargo
    FROM tbl_usuario u
    INNER JOIN tbl_funcionario f
        ON u.id_usuario = f.id_usuario_fk 
    WHERE u.nome_usuario LIKE '%' + @nome + '%';
END
GO
--=================================================================================================
CREATE OR ALTER PROCEDURE P_buscarFuncionarioPorCargo
    @cargo VARCHAR(100) 
AS
BEGIN
    SET NOCOUNT ON;
    SELECT 
        u.nome_usuario,
        u.cpf,
        u.email,
        FORMAT(u.data_nascimento, 'dd/MM/yyyy') AS data_nascimento,
        f.id_matricula,
        f.cargo,
        f.salario
    FROM tbl_usuario u
    INNER JOIN tbl_funcionario f
        ON u.id_usuario = f.id_usuario_fk  
    WHERE f.cargo = @cargo;                
END
GO
--=================================================================================================
CREATE OR ALTER PROCEDURE P_BuscarFuncionarioEmail
    @email VARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;
    SELECT
        u.nome_usuario,
        u.cpf,
        u.email,
        FORMAT(u.data_nascimento, 'dd/MM/yyyy') AS data_nascimento,
        f.id_matricula,
        f.cargo,
        f.salario
    FROM tbl_usuario u 
    INNER JOIN tbl_funcionario f
        ON u.id_usuario = f.id_usuario_fk
    WHERE u.email LIKE '%' + @email + '%';
END
GO
--=================================================================================================
CREATE OR ALTER PROCEDURE P_BuscarFuncionarioCpf
    @cpf CHAR(11) 
AS
BEGIN
    SET NOCOUNT ON;
    SELECT
        u.nome_usuario,
        u.cpf,
        u.email,
        FORMAT(u.data_nascimento, 'dd/MM/yyyy') AS data_nascimento,
        f.id_matricula,
        f.cargo,
        f.salario
    FROM tbl_usuario u 
    INNER JOIN tbl_funcionario f
        ON u.id_usuario = f.id_usuario_fk
    WHERE u.cpf = @cpf;
END
GO
--=================================================================================================
CREATE OR ALTER PROCEDURE P_BuscarFuncionarioDataNasc
    @data_nascimento DATE
AS
BEGIN
    SET NOCOUNT ON;
    SELECT
        u.nome_usuario,
        u.cpf,
        u.email,
        FORMAT(u.data_nascimento, 'dd/MM/yyyy') AS data_nascimento,-- o sql nao altera p padrao entao tenq formatar 
        f.id_matricula,
        f.cargo,
        f.salario
    FROM tbl_usuario u 
    INNER JOIN tbl_funcionario f
        ON u.id_usuario = f.id_usuario_fk
    WHERE u.data_nascimento = @data_nascimento;
END
GO
--=================================================================================================
CREATE OR ALTER PROCEDURE P_aumento
    @salario DECIMAL(10,2),
    @id_funcionario INT
AS
BEGIN
    SET NOCOUNT ON;

    IF (@salario <= 0)
    THROW 50002,'VALOR DO AUMENTO INVALIDO',1;

    IF EXISTS (SELECT 1 FROM tbl_funcionario WHERE id_matricula = @id_funcionario)
        BEGIN
            BEGIN TRY
                BEGIN TRANSACTION
                    UPDATE tbl_funcionario
                    SET salario = salario + @salario
                    WHERE id_matricula = @id_funcionario
                    PRINT 'AUMENTO REALIZADO'
                COMMIT;
            END TRY
            BEGIN CATCH
                ROLLBACK;
                THROW;
            END CATCH
        END
    ELSE
        THROW 50001, 'funcionario nao encontrado', 1;
END
GO
--=================================================================================================
CREATE OR ALTER PROCEDURE P_promocao
    @salario DECIMAL(10,2),
    @id_funcionario INT,
    @cargo VARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;

    IF @salario <= 0
    THROW 50002,'SALARIO INVALIDO',1;


    IF EXISTS (SELECT 1 FROM tbl_funcionario WHERE id_matricula = @id_funcionario)
        BEGIN
            BEGIN TRY
                BEGIN TRANSACTION
                    UPDATE tbl_funcionario
                    SET salario = @salario,
                    cargo = @cargo
                    WHERE id_matricula = @id_funcionario
                    PRINT 'PROMOCAO REALIZADA'
                COMMIT;
            END TRY
            BEGIN CATCH
                ROLLBACK;
                THROW;
            END CATCH
        END
    ELSE
        THROW 50001, 'funcionario nao encontrado', 1;
END
GO
--=================================================================================================
CREATE OR ALTER PROCEDURE P_atualizarSenhaFuncionario
    @id_usuario INT, 
    @senha VARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;

    IF EXISTS (
        SELECT 1
        FROM tbl_usuario u
        INNER JOIN tbl_funcionario f
        ON u.id_usuario = f.id_usuario_fk
        WHERE u.id_usuario = @id_usuario
    )
        IF EXISTS (SELECT 1 FROM tbl_usuario WHERE id_usuario = @id_usuario AND senha = @senha)
            THROW 50001, 'senha NAO PODE SER IGUAL A ANTERIOR', 1;
        ELSE
            BEGIN TRY
                BEGIN TRANSACTION
                    UPDATE tbl_usuario 
                    SET senha = @senha
                    WHERE id_usuario = @id_usuario
                COMMIT;
            END TRY
            BEGIN CATCH
                ROLLBACK;
                THROW; 
            END CATCH
    ELSE
        THROW 50002, 'funcionario nao encontrado', 1;
END
GO
--=================================================================================================
CREATE OR ALTER PROCEDURE P_atualizarEmailFuncionario
    @id_usuario INT,
    @email VARCHAR(100),
    @senha VARCHAR(100)
AS
    BEGIN
        SET NOCOUNT ON;
           IF EXISTS (
            SELECT 1
            FROM tbl_usuario u
            INNER JOIN tbl_funcionario f
            ON u.id_usuario = f.id_usuario_fk
            WHERE U.id_usuario = @id_usuario 
            ) 
                IF EXISTS (SELECT 1 FROM tbl_usuario WHERE  email = @email)
                THROW 50002, 'EMAIL JA CADASTRADO', 1;
                ELSE

                IF EXISTS (SELECT 1 FROM tbl_usuario WHERE id_usuario = @id_usuario AND email = @email)
                THROW 50001, 'EMAIL NAO PODE SER IGUAL AO ANTERIOR', 1;
                ELSE

                BEGIN TRY
                        BEGIN TRANSACTION
                        UPDATE tbl_usuario 
                        SET EMAIL = @email,
                        senha = @senha
                        WHERE id_usuario = @id_usuario
                        COMMIT;
                END TRY
                BEGIN CATCH
                        ROLLBACK;
                        THROW; 
                END CATCH
            ELSE
                THROW 50002, 'funcionario nao encontrado ', 1;
    END
GO
--=================================================================================================
CREATE OR ALTER PROCEDURE P_cadastroFuncionario
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
    @tipo VARCHAR(50),
    @cargo VARCHAR(50),
    @salario DECIMAL(10,2)
AS
BEGIN
    DECLARE @id_uf INT
    DECLARE @id_cidade INT
    DECLARE @id_endereco INT
    DECLARE @id_usuario INT

    BEGIN TRY
        BEGIN TRANSACTION

            IF EXISTS (SELECT 1 FROM tbl_usuario WHERE email = @email)
            THROW 50001,'EMAIL JA ESTA CADASTRADO',1;

            IF EXISTS (SELECT 1 FROM tbl_usuario WHERE cpf = @cpf)
            THROW 50002,'CPF JA ESTA CADASTRADO',1;

            IF(@salario <900)
            THROW 50003,'SALARIO INCORRETO NO MINIMO DEVE SER 900',1;

            SET @id_uf = (SELECT id_uf FROM tbl_uf WHERE uf = @uf)
            IF @id_uf IS NULL
            THROW 50004, 'UF NAO ENCONTRADA', 1;

            -- 2. busca ou insere cidade
            SET @id_cidade = (SELECT id_cidade FROM tbl_cidade WHERE cidade = @cidade AND id_uf_fk = @id_uf)
            IF @id_cidade IS NULL
            BEGIN
                INSERT INTO tbl_cidade (cidade, id_uf_fk) VALUES (@cidade, @id_uf)
                SET @id_cidade = SCOPE_IDENTITY()
            END

            -- 3. insere endereco
            INSERT INTO tbl_endereco (logradouro, cep, bairro, status_endereco, id_cidadeFK)
            VALUES (@logradouro, @cep, @bairro, 'ATIVO', @id_cidade)
            SET @id_endereco = SCOPE_IDENTITY()

            -- 4. insere usuario
            INSERT INTO tbl_usuario (nome_usuario, cpf, email, senha, data_nascimento, numero_residencia, complemento, id_endereco_fk)
            VALUES (@nome, @cpf, @email, @senha, @data_nascimento, @numero_residencia, @complemento, @id_endereco)
            SET @id_usuario = SCOPE_IDENTITY()

            -- 5. insere telefone
            INSERT INTO tbl_telefone (telefone, tipo, status_telefone, id_usuario_fk)
            VALUES (@telefone, @tipo, 'ATIVO', @id_usuario)

            -- 6. insere funcionario
            INSERT INTO tbl_funcionario (cargo, salario, id_usuario_fk)
            VALUES (@cargo, @salario, @id_usuario)

        COMMIT
        PRINT 'Funcionário cadastrado com sucesso'

    END TRY
    BEGIN CATCH
        ROLLBACK
        PRINT 'Erro: ' + ERROR_MESSAGE()
    END CATCH
END
GO
--=================================================================================================
CREATE OR ALTER PROCEDURE P_excluirFuncionario
    @id_funcionario INT
AS 
    BEGIN
        SET NOCOUNT ON;

        IF NOT EXISTS(SELECT 1 FROM tbl_funcionario WHERE id_matricula = @id_funcionario)
            THROW 50002, 'FUNCIONARIO NAO ENCONTRADO', 1;

        IF EXISTS(SELECT 1  FROM tbl_emprestimo WHERE id_funcionariofk = @id_funcionario )
        THROW 50001,'FUNCIONARIO NAO PODE SER excluido ',1;

        BEGIN TRY
            BEGIN TRANSACTION
                DELETE FROM tbl_funcionario 
                WHERE id_matricula = @id_funcionario
                PRINT 'FUNCIONARIO EXCLUIDO'
            COMMIT;
            
        END TRY
        BEGIN CATCH
            ROLLBACK;
            THROW;
        END CATCH
    END
GO

CREATE OR ALTER TRIGGER TR_ExcluirFunc
ON tbl_funcionario
AFTER DELETE
AS
BEGIN
    SET NOCOUNT ON;

    BEGIN TRY

        /*
            A tabela DELETED contém os funcionários
            que acabaram de ser removidos.

            Objetivo da trigger:
            1. Excluir os telefones do usuário.
            2. Excluir o usuário.
            3. Excluir o endereço SOMENTE se nenhum
               outro usuário estiver utilizando-o.
        */

        -- Guarda os endereços dos usuários excluídos
        DECLARE @Enderecos TABLE
        (
            id_endereco INT
        );

        INSERT INTO @Enderecos (id_endereco)
        SELECT u.id_endereco_fk
        FROM tbl_usuario u
        INNER JOIN deleted d
            ON u.id_usuario = d.id_usuario_fk;

        -- Remove os telefones vinculados ao usuário
        DELETE t
        FROM tbl_telefone t
        INNER JOIN deleted d
            ON t.id_usuario_fk = d.id_usuario_fk;

        -- Remove os usuários vinculados ao funcionário
        DELETE u
        FROM tbl_usuario u
        INNER JOIN deleted d
            ON u.id_usuario = d.id_usuario_fk;

        /*
            Remove apenas os endereços que não
            possuem mais usuários vinculados.
        */
        DELETE e
        FROM tbl_endereco e
        INNER JOIN @Enderecos ed
            ON e.id_endereco = ed.id_endereco
        WHERE NOT EXISTS
        (
            SELECT 1
            FROM tbl_usuario u
            WHERE u.id_endereco_fk = e.id_endereco
        );

    END TRY
    BEGIN CATCH
        THROW;
    END CATCH
END
GO
--=================================================================================================


SELECT * FROM tbl_endereco;

SELECT * FROM tbl_livro;

SELECT * FROM tbl_usuario;

SELECT * FROM tbl_cliente;

SELECT * FROM tbl_funcionario;

SELECT * FROM tbl_telefone;

SELECT * FROM tbl_emprestimo;



