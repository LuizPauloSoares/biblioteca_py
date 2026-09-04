USE bancoPython
GO



--=================================================================================================
CREATE OR ALTER PROCEDURE P_pesquisaNumero
    @numero CHAR(11)
AS
    BEGIN
        SET NOCOUNT ON;
        IF NOT EXISTS(SELECT 1 FROM tbl_telefone WHERE telefone = @numero)
        THROW 50001,'numero NAO EXISTE',1;
        
        SELECT
            u.id_usuario,
            u.nome_usuario,
            u.cpf,
            u.email,
            u.data_nascimento,
            t.telefone,
            t.status_telefone,
            t.tipo
        FROM tbl_usuario u 
        INNER JOIN tbl_telefone t
            ON u.id_usuario = t.id_usuario_fk
        WHERE t.telefone = @numero;
    END
GO
--=================================================================================================
CREATE OR ALTER PROCEDURE P_pesquisaNumeroNome
    @nome VARCHAR(100)
AS
    BEGIN
        SET NOCOUNT ON;
        IF NOT EXISTS(SELECT 1 FROM tbl_usuario WHERE nome_usuario LIKE '%' + @nome + '%')
        THROW 50001, 'usuario nao encontrado', 1;
        
        SELECT
            u.id_usuario,
            u.nome_usuario,
            u.cpf,
            u.email,
            u.data_nascimento,
            t.telefone,
            t.status_telefone,
            t.tipo
        FROM tbl_usuario u 
        INNER JOIN tbl_telefone t
            ON u.id_usuario = t.id_usuario_fk
        WHERE u.nome_usuario LIKE '%' + @nome + '%';
    END
GO
--=================================================================================================
CREATE OR ALTER PROCEDURE P_pesquisaTelefoneTipo
    @tipo VARCHAR(50) 
AS
    BEGIN
        SET NOCOUNT ON;
        IF NOT EXISTS(SELECT 1 FROM tbl_telefone WHERE tipo =  @tipo)
        THROW 50001, 'telefone nao encontrado', 1;

                SELECT
            u.id_usuario,
            u.nome_usuario,
            u.cpf,
            u.email,
            u.data_nascimento,
            t.telefone,
            t.status_telefone,
            t.tipo
        FROM tbl_usuario u 
        INNER JOIN tbl_telefone t
            ON u.id_usuario = t.id_usuario_fk
        WHERE t.tipo = @tipo;
        
    END
GO
--=================================================================================================
CREATE OR ALTER PROCEDURE P_pesquisaTelefonestatus
    @status_telefone VARCHAR(50)
AS
    BEGIN
        SET NOCOUNT ON;
        IF NOT EXISTS(SELECT 1 FROM tbl_telefone WHERE status_telefone =  @status_telefone)
        THROW 50001, 'telefone nao encontrado', 1;

                SELECT
            u.id_usuario,
            u.nome_usuario,
            u.cpf,
            u.email,
            u.data_nascimento,
            t.telefone,
            t.status_telefone,
            t.tipo
        FROM tbl_usuario u 
        INNER JOIN tbl_telefone t
            ON u.id_usuario = t.id_usuario_fk
        WHERE t.status_telefone = @status_telefone;
        
    END
GO
--=================================================================================================
CREATE OR ALTER PROCEDURE P_atualizarTelefone
    @id_telefone    INT,
    @telefone       CHAR(11),
    @tipo           VARCHAR(50)
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT EXISTS (SELECT 1 FROM tbl_telefone WHERE id_telefone = @id_telefone)
        THROW 50001, 'Telefone nao encontrado', 1;

    IF EXISTS (SELECT 1 FROM tbl_telefone WHERE telefone = @telefone AND id_telefone <> @id_telefone)
        THROW 50002, 'Numero ja cadastrado para outro usuario', 1;

    BEGIN TRY
        BEGIN TRANSACTION
            UPDATE tbl_telefone
            SET telefone = @telefone,
                tipo     = @tipo
            WHERE id_telefone = @id_telefone;
        COMMIT;
    END TRY
    BEGIN CATCH
        ROLLBACK;
        THROW;
    END CATCH
END
GO

-- ============================================================
CREATE OR ALTER PROCEDURE P_atualizarStatusTelefone
    @id_telefone    INT,
    @status         VARCHAR(50)
AS
BEGIN
    SET NOCOUNT ON;
    IF NOT EXISTS (SELECT 1 FROM tbl_telefone WHERE id_telefone = @id_telefone)
        THROW 50001, 'Telefone nao encontrado', 1;

    IF @status NOT IN ('ATIVO', 'INATIVO')-- DA PRA M UDAR E NO BACK SO ENVIA ESSES DOIS 
        THROW 50002, 'Status invalido — use ATIVO ou INATIVO', 1;

    BEGIN TRY
        BEGIN TRANSACTION
            UPDATE tbl_telefone
            SET status_telefone = @status
            WHERE id_telefone = @id_telefone;
        COMMIT;
    END TRY
    BEGIN CATCH
        ROLLBACK;
        THROW;
    END CATCH
END
GO

-- ============================================================
CREATE OR ALTER PROCEDURE P_excluirTelefone
    @id_telefone INT
AS
BEGIN
    SET NOCOUNT ON;
    IF NOT EXISTS (SELECT 1 FROM tbl_telefone WHERE id_telefone = @id_telefone)
        THROW 50001, 'Telefone nao encontrado', 1;

    DECLARE @id_usuario INT;
    SELECT @id_usuario = id_usuario_fk FROM tbl_telefone WHERE id_telefone = @id_telefone;


    IF (SELECT COUNT(*) FROM tbl_telefone 
        WHERE id_usuario_fk = @id_usuario ) = 1
        THROW 50002, 'Usuario possui apenas um telefone ativo — nao e possivel EXCLUIR este telefone', 1;

    IF (SELECT COUNT(*) FROM tbl_telefone 
        WHERE id_usuario_fk = @id_usuario  AND status_telefone = 'ATIVO') = 1--tenq validar ain
        THROW 50002, 'Usuario possui apenas um telefone ativo — nao e possivel EXCLUIR este telefone', 1;

    BEGIN TRY
        BEGIN TRANSACTION
            DELETE FROM  tbl_telefone
            WHERE id_telefone = @id_telefone;
        COMMIT;
    END TRY
    BEGIN CATCH
        ROLLBACK;
        THROW;
    END CATCH
END
GO
--====================================================================================================
CREATE OR ALTER PROCEDURE P_cadastrarNum
	@tipo VARCHAR(50), 
	@telefone CHAR(11),
	@id_usuario_fk INT 
AS 
    BEGIN   
        SET NOCOUNT ON;

            IF EXISTS(SELECT 1 FROM tbl_telefone WHERE id_usuario_fk = @id_usuario_fk AND telefone = @telefone)
            THROW 50001 ,'TELEFONE JA PERTENCE A ESTE USUARIO',1;

            IF NOT EXISTS(SELECT 1 FROM tbl_usuario WHERE id_usuario = @id_usuario_fk )
            THROW 50002 ,' USUARIO NAO ENCONTRADO ',1;
        
            BEGIN TRY
                BEGIN TRANSACTION
                    INSERT INTO tbl_telefone (tipo,status_telefone,telefone,id_usuario_fk)VALUES
                    (@tipo,'ATIVO',@telefone,@id_usuario_fk)

                    COMMIT

            END TRY
            BEGIN CATCH
                ROLLBACK;
                THROW;
            END CATCH
    END
GO

--====================================================================================================
EXEC P_pesquisaNumero @numero = '11887788888';
GO

EXEC P_pesquisaNumeroNome @nome = 'João';
GO

EXEC P_pesquisaTelefoneTipo @tipo = 'CELULAR';
GO

EXEC P_pesquisaTelefonestatus @status_telefone = 'ATIVO';
GO

EXEC P_atualizarTelefone 
    @id_telefone = 1,
    @telefone    = '11887788888',
    @tipo        = 'CELULAR';
GO

EXEC P_atualizarStatusTelefone 
    @id_telefone = 2,
    @status      = 'INATIVO';
GO

EXEC P_excluirTelefone @id_telefone = 1;

GO

SELECT * FROM  tbl_telefone
