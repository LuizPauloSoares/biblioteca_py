USE bancoPython
GO


CREATE OR ALTER PROCEDURE P_Emprestimo(
    @id_livrofk       INT,
    @id_clientefk     INT,  
    @id_funcionariofk INT  
)
AS
BEGIN
    SET NOCOUNT ON;

    BEGIN TRY
        BEGIN TRAN;
        IF NOT EXISTS (
            SELECT 1 FROM tbl_livro WHERE id_livro = @id_livrofk
        )
        BEGIN
            THROW 50002, 'Livro não encontrado', 1;
        END

        IF NOT EXISTS (
            SELECT 1 FROM tbl_cliente WHERE id_cliente = @id_clientefk
        )
        BEGIN
            THROW 50003, 'Cliente não encontrado', 1;
        END

        IF NOT EXISTS (
            SELECT 1 FROM tbl_funcionario WHERE id_matricula = @id_funcionariofk
        )
        BEGIN
            THROW 50004, 'Funcionário não encontrado', 1;
        END

        IF EXISTS (
            SELECT 1 
            FROM tbl_livro 
            WHERE id_livro = @id_livrofk
              AND qnt_livro <= 0
        )
        BEGIN
            THROW 50001, 'Livro sem estoque disponível', 1;
        END

        INSERT INTO tbl_emprestimo (
            data_emprestimo,
            data_previsao,
            status_emprestimo,
            id_livrofk,
            id_clientefk,
            id_funcionariofk
        )
        VALUES (
            CAST(GETDATE() AS DATE),
            DATEADD(DAY, 7, CAST(GETDATE() AS DATE)),
            'ativo',
            @id_livrofk,
            @id_clientefk,
            @id_funcionariofk
        );
        COMMIT 

    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0 --seve pra dar rollback so se tesiver uma transiçao se nao tiver nao faz nada
            ROLLBACK;

        THROW;
    END CATCH
END
GO

CREATE OR ALTER TRIGGER T_aluguelLivro
    ON  tbl_emprestimo
AFTER INSERT
AS
    BEGIN
        SET NOCOUNT ON;
        BEGIN TRY
            UPDATE tbl_livro
            SET qnt_livro = qnt_livro - 1
            WHERE id_livro = (SELECT id_livrofk FROM INSERTED)

            
        END TRY
        BEGIN CATCH
            THROW;
      
        END CATCH
    END
GO
--=================================================================================================
CREATE OR ALTER PROCEDURE P_Devolucao (
    @id_livrofk   INT,
    @id_clientefk INT 
)
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT EXISTS (
        SELECT 1 
        FROM tbl_emprestimo 
        WHERE id_livrofk  = @id_livrofk 
          AND id_clientefk = @id_clientefk 
          AND data_devolucao IS NULL
    )
    BEGIN
        THROW 50001, 'Nenhum emprestimo ativo encontrado', 1;
    END

    BEGIN TRY
        BEGIN TRANSACTION;

        UPDATE tbl_emprestimo
        SET data_devolucao    = CAST(GETDATE() AS DATE)
        WHERE id_livrofk   = @id_livrofk 
          AND id_clientefk  = @id_clientefk 
          AND data_devolucao IS NULL;

        PRINT 'livro devolvido com sucesso'

        COMMIT;
    END TRY
    BEGIN CATCH
        ROLLBACK;
        THROW;
    END CATCH
END;
GO

CREATE or ALTER TRIGGER TR_Devolucao
ON tbl_emprestimo
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    IF UPDATE(data_devolucao)
    BEGIN
        BEGIN TRY
            UPDATE tbl_livro
            SET qnt_livro = qnt_livro + 1
            WHERE id_livro = (SELECT id_livrofk FROM inserted WHERE data_devolucao IS NOT NULL)

            --ve se teve atraso
            IF (SELECT data_devolucao FROM inserted) > (SELECT data_previsao FROM inserted)
                UPDATE tbl_emprestimo
                SET status_emprestimo = 'atrasado'
                WHERE id_emprestimo = (SELECT id_emprestimo FROM inserted)
            ELSE
                UPDATE tbl_emprestimo
                SET status_emprestimo = 'devolvido'
                WHERE id_emprestimo = (SELECT id_emprestimo FROM inserted)
        END TRY
        BEGIN CATCH
            THROW; 
        END CATCH
    END
END
GO
--=================================================================================================

CREATE OR ALTER PROCEDURE P_excluirLivro (
    @id_livrofk INT
)
AS
BEGIN
    SET NOCOUNT ON;

    BEGIN TRY
        BEGIN TRANSACTION;

            IF NOT EXISTS (SELECT 1 FROM tbl_livro WHERE id_livro = @id_livrofk)
                THROW 50005, 'LIVRO INEXISTENTE', 1;

            IF EXISTS (SELECT 1 FROM tbl_emprestimo WHERE id_livrofk = @id_livrofk)
                THROW 50004, 'Livro possui emprestimos, nao pode excluir', 1;

            DELETE FROM tbl_livro WHERE id_livro = @id_livrofk;
            PRINT 'Excluido com sucesso';

        COMMIT;

    END TRY
    BEGIN CATCH
        ROLLBACK;
        THROW;
    END CATCH
END
GO
--=================================================================================================
CREATE OR ALTER PROCEDURE P_AtualizarQntLivro
    @id_livro INT,
    @qnt INT
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT EXISTS (
        SELECT 1 
        FROM tbl_livro 
        WHERE id_livro = @id_livro
    )
    BEGIN
        THROW 50002, 'Livro não encontrado', 1;
    END


    IF (@qnt < 0)
    BEGIN
        THROW 50003, 'Quantidade não pode ser negativa', 1;
    END

    BEGIN TRY
        BEGIN TRANSACTION; -- inicia a transacao

            UPDATE tbl_livro
            SET qnt_livro =qnt_livro + @qnt
            WHERE id_livro = @id_livro;

            PRINT 'Quantidade atualizada com sucesso';

        COMMIT; 
    END TRY
    BEGIN CATCH
        ROLLBACK;
        THROW;   
    END CATCH
END;
GO
--=================================================================================================
CREATE OR ALTER PROCEDURE P_pesquisaAutor
    @autor VARCHAR(100)

AS
    BEGIN
        SET NOCOUNT ON;

        SELECT * FROM tbl_livro 
        WHERE autor LIKE '%'+ @autor +'%'
    END
GO
--=================================================================================================
CREATE OR ALTER PROCEDURE P_pesquisaEditora
    @editora VARCHAR (50)

AS
    BEGIN
        SET NOCOUNT ON;

        SELECT * FROM tbl_livro 
        WHERE editora LIKE '%'+ @editora +'%'
    END
GO
--=================================================================================================
CREATE OR ALTER PROCEDURE P_pesquisaGenero
    @genero VARCHAR (50)

AS
    BEGIN
        SET NOCOUNT ON;

        SELECT * FROM tbl_livro 
        WHERE genero LIKE '%'+ @genero +'%'
    END
GO
--=================================================================================================
CREATE OR ALTER PROCEDURE P_pesquisaAno
    @ano_lancamento INT

AS
    BEGIN
        SET NOCOUNT ON;

        SELECT * FROM tbl_livro 
        WHERE ano_lancamento = @ano_lancamento
    END
GO
    
USE bancoPython;
GO
--=======================================================================================================


--testes

EXEC P_Devolucao 
    @id_livrofk = 2,
    @id_clientefk = 1;
GO

EXEC P_AtualizarQntLivro 
    @id_livro = 5,
    @qnt = 10;
GO

EXEC P_pesquisaAutor @autor = 'Machado ';
GO

EXEC P_pesquisaEditora @editora = 'Saraiva';
GO

EXEC P_pesquisaGenero @genero = 'Romance';
GO

PRINT 'TESTE P_pesquisaAno';
EXEC P_pesquisaAno @ano_lancamento = 2015;
GO

EXEC P_excluirLivro 
    @id_livrofk = 1; 
GO

EXEC P_Emprestimo 
    @id_livrofk = 2,
    @id_clientefk = 4,
    @id_funcionariofk = 1;


SELECT * FROM tbl_livro;
SELECT * FROM tbl_emprestimo;

GO
