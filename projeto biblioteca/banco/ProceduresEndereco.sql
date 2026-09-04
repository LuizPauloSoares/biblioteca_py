USE bancoPython
GO



CREATE OR ALTER PROCEDURE P_desativarEndereco
    @id_endereco INT
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT EXISTS (SELECT 1 FROM tbl_endereco WHERE id_endereco = @id_endereco)
        THROW 50001, 'Endereco nao encontrado', 1;

    BEGIN TRY
        BEGIN TRANSACTION

            UPDATE tbl_endereco
            SET status_endereco = 'INATIVO'
            WHERE id_endereco = @id_endereco;

        COMMIT;
    END TRY
    BEGIN CATCH
        ROLLBACK;
        THROW;
    END CATCH
END
GO
-- ============================================================

CREATE OR ALTER  PROCEDURE P_atualizarEndereco
    @id_usuario       INT,
    @logradouro       VARCHAR(100),
    @cep              CHAR(9),
    @bairro           VARCHAR(100),
    @cidadeCliente    VARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT EXISTS (SELECT 1 FROM tbl_usuario WHERE id_usuario = @id_usuario)
        THROW 50001, 'Usuario nao encontrado', 1;

    DECLARE @id_cidade INT;
    SELECT @id_cidade = id_cidade FROM tbl_cidade WHERE cidade = @cidadeCliente;

    IF @id_cidade IS NULL
        THROW 50002, 'Cidade nao encontrada', 1;

    BEGIN TRY
        BEGIN TRANSACTION

            UPDATE tbl_endereco
            SET status_endereco = 'INATIVO'
            WHERE id_endereco = (
                SELECT id_endereco_fk FROM tbl_usuario WHERE id_usuario = @id_usuario
            );

            INSERT INTO tbl_endereco (logradouro, cep, bairro, status_endereco, id_cidadeFK)
            VALUES (@logradouro, @cep, @bairro, 'ATIVO', @id_cidade);

            UPDATE tbl_usuario
            SET id_endereco_fk = SCOPE_IDENTITY()
            WHERE id_usuario = @id_usuario;

        COMMIT;
    END TRY
    BEGIN CATCH
        ROLLBACK;
        THROW;
    END CATCH
END
GO
-- ============================================================

CREATE OR ALTER  PROCEDURE P_excluirEndereco
    @id_endereco INT
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT EXISTS (SELECT 1 FROM tbl_endereco WHERE id_endereco = @id_endereco)
        THROW 50001, 'Endereco nao encontrado', 1;

    -- Impede inativar um endereco que ainda esta vinculado a um usuario ativo
    IF EXISTS (SELECT 1 FROM tbl_usuario WHERE id_endereco_fk = @id_endereco)
        THROW 50002, 'Endereco vinculado a um usuario ativo', 1;

    BEGIN TRY
        BEGIN TRANSACTION
            UPDATE tbl_endereco
            SET status_endereco = 'INATIVO'
            WHERE id_endereco = @id_endereco;
        COMMIT;
    END TRY
    BEGIN CATCH
        ROLLBACK;
        THROW;
    END CATCH
END
GO
-- ============================================================

CREATE OR ALTER  PROCEDURE P_listarEnderecoUsuario
    @id_usuario INT
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT EXISTS (SELECT 1 FROM tbl_usuario WHERE id_usuario = @id_usuario)
        THROW 50001, 'Usuario nao encontrado', 1;

    SELECT
        u.id_usuario,
        u.nome_usuario,
        u.numero_residencia,
        u.complemento,
        e.logradouro,
        e.cep,
        e.bairro,
        e.status_endereco,
        c.cidade,
        uf.uf,
        uf.estado
    FROM tbl_usuario u
    INNER JOIN tbl_endereco e
        ON u.id_endereco_fk = e.id_endereco
    INNER JOIN tbl_cidade c
        ON e.id_cidadeFK = c.id_cidade
    INNER JOIN tbl_uf uf
        ON c.id_uf_fk = uf.id_uf
    WHERE u.id_usuario = @id_usuario;
END
GO
-- ============================================================

CREATE OR ALTER  PROCEDURE P_verificarCep
    @cep CHAR(9)
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT EXISTS (SELECT 1 FROM tbl_endereco WHERE cep = @cep)
        THROW 50001, 'CEP nao encontrado', 1;

    SELECT
        e.id_endereco,
        e.logradouro,
        e.cep,
        e.bairro,
        e.status_endereco,
        c.cidade,
        u.uf,
        u.estado
    FROM tbl_endereco e
    INNER JOIN tbl_cidade c
        ON e.id_cidadeFK = c.id_cidade
    INNER JOIN tbl_uf u
        ON c.id_uf_fk = u.id_uf
    WHERE e.cep = @cep;
END
GO
-- ============================================================

CREATE OR ALTER  PROCEDURE P_verificarBairro
    @bairro VARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT EXISTS (SELECT 1 FROM tbl_endereco WHERE bairro LIKE '%' + @bairro + '%')
        THROW 50001, 'Bairro nao encontrado', 1;

    SELECT
        e.id_endereco,
        e.logradouro,
        e.cep,
        e.bairro,
        e.status_endereco,
        c.cidade,
        u.uf,
        u.estado
    FROM tbl_endereco e
    INNER JOIN tbl_cidade c
        ON e.id_cidadeFK = c.id_cidade
    INNER JOIN tbl_uf u
        ON c.id_uf_fk = u.id_uf
    WHERE e.bairro LIKE '%' + @bairro + '%';
END
GO
-- ============================================================

CREATE OR ALTER  PROCEDURE P_verificarLogradouro
    @logradouro VARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT EXISTS (SELECT 1 FROM tbl_endereco WHERE logradouro LIKE '%' + @logradouro + '%')
        THROW 50001, 'Logradouro nao encontrado', 1;

    SELECT
        e.id_endereco,
        e.logradouro,
        e.cep,
        e.bairro,
        e.status_endereco,
        c.cidade,
        u.uf,
        u.estado
    FROM tbl_endereco e
    INNER JOIN tbl_cidade c
        ON e.id_cidadeFK = c.id_cidade
    INNER JOIN tbl_uf u
        ON c.id_uf_fk = u.id_uf
    WHERE e.logradouro LIKE '%' + @logradouro + '%';
END
GO
-- ============================================================

CREATE OR ALTER  PROCEDURE P_verificarUf
    @uf CHAR(2)
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT EXISTS (SELECT 1 FROM tbl_uf WHERE uf = @uf)
        THROW 50001, 'UF nao encontrada', 1;

    SELECT
        e.id_endereco,
        e.logradouro,
        e.cep,
        e.bairro,
        e.status_endereco,
        c.cidade,
        u.uf,
        u.estado
    FROM tbl_endereco e
    INNER JOIN tbl_cidade c
        ON e.id_cidadeFK = c.id_cidade
    INNER JOIN tbl_uf u
        ON c.id_uf_fk = u.id_uf
    WHERE u.uf = @uf;
END
GO

-- ============================================================
CREATE OR ALTER  PROCEDURE P_verificarCidade
    @cidade VARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT EXISTS (SELECT 1 FROM tbl_cidade WHERE cidade LIKE '%' + @cidade + '%')
        THROW 50001, 'Cidade nao encontrada', 1;

    SELECT
        e.id_endereco,
        e.logradouro,
        e.cep,
        e.bairro,
        e.status_endereco,
        c.cidade,
        u.uf,
        u.estado
    FROM tbl_endereco e
    INNER JOIN tbl_cidade c
        ON e.id_cidadeFK = c.id_cidade
    INNER JOIN tbl_uf u
        ON c.id_uf_fk = u.id_uf
    WHERE c.cidade LIKE '%' + @cidade + '%';
END
GO
--============================================================

SELECT * FROM tbl_uf;

SELECT * FROM tbl_cidade;

SELECT * FROM tbl_endereco;

SELECT * FROM tbl_livro;

SELECT * FROM tbl_usuario;

SELECT * FROM tbl_cliente;

SELECT * FROM tbl_funcionario;

SELECT * FROM tbl_telefone;

SELECT * FROM tbl_emprestimo;

