from conexao.Conexao import conexao
from classes.Livro import Livro

class LivroDAO:

    @staticmethod
    def selecionar_todos():
        sql = "SELECT * FROM tbl_livro"
        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql)
            linhas_brutas = cursor.fetchall()

            lista = []
            for linha in linhas_brutas:
                id      = linha[0]
                titulo  = linha[1]
                autor   = linha[2]
                ano     = linha[3]
                editora = linha[4]
                genero  = linha[5]
                qnt     = linha[6]
                linhas = (f"id: {id} - titulo: {titulo} - autor: {autor} - ano: {ano} - editora: {editora} - genero: {genero} - quantidade: {qnt} \n ")
                lista.append(linhas)    
            return lista
        except Exception as e:
            print(f"Erro ao processar o SELECT: {e}")
            return []

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def verificar_livro(titulo):
        sql = "SELECT * FROM tbl_livro WHERE titulo LIKE ?"
        valores = (f"%{titulo}%",)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            resposta = cursor.fetchone()

            if resposta is None:

                return None
            else:
                id      = resposta[0]
                titulo  = resposta[1]
                autor   = resposta[2]
                ano     = resposta[3]
                editora = resposta[4]
                genero  = resposta[5]
                qnt     = resposta[6]
                print(f"id: {id} - titulo: {titulo} - autor: {autor} - ano: {ano} - editora: {editora} - genero: {genero} - quantidade: {qnt}")
                return resposta

        except Exception as e:
            print(f"Erro ao processar o Select: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def verificar_id(id):
        sql = "SELECT * FROM tbl_livro where id_livro = ?"
        valor = (id,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valor)
            resposta = cursor.fetchone()

            if resposta:
                return resposta
            else:
                return None

        except Exception as e:
            print(f"Erro ao processar o Select: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def cadastro_livro(livro):
        titulo         = livro.getTitulo()
        autor          = livro.getAutor()
        ano_lancamento = livro.getAno_lancamento()
        editora        = livro.getEditora()
        genero         = livro.getGenero()
        qnt            = livro.getQnt_livro()

        test = LivroDAO.verificar_livro(titulo)

        if test is not None:
            print("livro ja cadastrado")
        else:
            sql = "INSERT INTO tbl_livro (titulo, autor, ano_lancamento, editora, genero, qnt_livro) VALUES (?, ?, ?, ?, ?, ?)" 
            valores = (titulo, autor, ano_lancamento, editora, genero, qnt)

            try:
                conn = conexao.get_connection()
                cursor = conn.cursor()
                cursor.execute(sql, valores)
                conn.commit()
                return "livro cadastrado com sucesso"

            except Exception as e:
                print(f"Erro ao processar o Insert: {e}")
                return None

            finally:
                if 'conn' in locals():
                    conn.close()

    @staticmethod
    def emprestar_livro(idLivro, idUsuario, idFuncionario):
        livro = LivroDAO.verificar_id(idLivro)

        if livro is None:
            print("Livro não cadastrado")
            return

        if livro[6] <= 0: 
            print("Livro indisponível")
            return

        sql = "EXEC P_Emprestimo ?, ?, ?"
        valores = (idLivro, idUsuario, idFuncionario)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            conn.commit()
            return "Livro emprestado com sucesso"

        except Exception as e:
            print(f"Erro ao processar o empréstimo: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def devolver_livro(idLivro, idUsuario):
        livro = LivroDAO.verificar_id(idLivro)

        if livro is None:
            print("livro nao cadastrado")
            return
        else:
            sql_devolucao = "EXEC P_Devolucao ?, ?"
            valores = (idLivro, idUsuario)

            try:
                conn = conexao.get_connection()
                cursor = conn.cursor()
                cursor.execute(sql_devolucao, valores)
                conn.commit()
                return "livro devolvido com sucesso"

            except Exception as e:
                print(f"Erro ao processar a atualizacao: {e}")
                return None

            finally:
                if 'conn' in locals():
                    conn.close()

    @staticmethod
    def excluir_livro(id):
        livro = LivroDAO.verificar_id(id)

        if livro is None:
            print("livro nao cadastrado")
            return
        else:
            sql = "EXEC P_excluirLivro ?" 
            valores = (id,)

            try:
                conn = conexao.get_connection()
                cursor = conn.cursor()
                cursor.execute(sql, valores)
                conn.commit()
                return "livro excluído com sucesso"

            except Exception as e:
                print(f"Erro ao processar a exclusao: {e}")
                return None

            finally:
                if 'conn' in locals():
                    conn.close()

    @staticmethod
    def atualizarQnt(id, qnt):
        sql = "EXEC P_AtualizarQntLivro ?, ?"
        valores = (id, qnt)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            conn.commit()
            print("livro atualizado com sucesso")

        except Exception as e:
            print(f"Erro ao processar a atualizacao: {e}")

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def pesquisar_autor(autor):
        sql = "EXEC P_pesquisaAutor ?"
        valores = (autor,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            linhas = cursor.fetchall()

            if not linhas:
                print("nenhum livro encontrado")
                return None

            for linha in linhas:
                id      = linha[0]
                titulo  = linha[1]
                autor   = linha[2]
                ano     = linha[3]
                editora = linha[4]
                genero  = linha[5]
                qnt     = linha[6]
                print(f"id: {id} - titulo: {titulo} - autor: {autor} - ano: {ano} - editora: {editora} - genero: {genero} - quantidade: {qnt}")

            return linhas

        except Exception as e:
            print(f"Erro ao pesquisar autor: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def pesquisar_editora(editora):
        sql = "EXEC P_pesquisaEditora ?"
        valores = (editora,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            linhas = cursor.fetchall()

            if not linhas:
                print("nenhum livro encontrado")
                return None

            for linha in linhas:
                id      = linha[0]
                titulo  = linha[1]
                autor   = linha[2]
                ano     = linha[3]
                editora = linha[4]
                genero  = linha[5]
                qnt     = linha[6]
                print(f"id: {id} - titulo: {titulo} - autor: {autor} - ano: {ano} - editora: {editora} - genero: {genero} - quantidade: {qnt}")

            return linhas

        except Exception as e:
            print(f"Erro ao pesquisar editora: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def pesquisar_genero(genero):
        sql = "EXEC P_pesquisaGenero ?"
        valores = (genero,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            linhas = cursor.fetchall()

            if not linhas:
                print("nenhum livro encontrado")
                return None

            for linha in linhas:
                id      = linha[0]
                titulo  = linha[1]
                autor   = linha[2]
                ano     = linha[3]
                editora = linha[4]
                genero  = linha[5]
                qnt     = linha[6]
                print(f"id: {id} - titulo: {titulo} - autor: {autor} - ano: {ano} - editora: {editora} - genero: {genero} - quantidade: {qnt}")

            return linhas

        except Exception as e:
            print(f"Erro ao pesquisar genero: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def pesquisar_ano(ano):
        sql = "EXEC P_pesquisaAno ?"
        valores = (ano,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            linhas = cursor.fetchall()

            if not linhas:
                print("nenhum livro encontrado")
                return None

            for linha in linhas:
                id      = linha[0]
                titulo  = linha[1]
                autor   = linha[2]
                ano     = linha[3]
                editora = linha[4]
                genero  = linha[5]
                qnt     = linha[6]
                print(f"id: {id} - titulo: {titulo} - autor: {autor} - ano: {ano} - editora: {editora} - genero: {genero} - quantidade: {qnt}")

            return linhas

        except Exception as e:
            print(f"Erro ao pesquisar ano: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()