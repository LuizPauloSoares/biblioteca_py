from conexao.Conexao import conexao
from classes.Telefone import Telefone

class TelefoneDAO:

    @staticmethod
    def buscar_por_numero(numero):
        sql = "EXEC P_pesquisaNumero ?"
        valor = (numero,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valor)

            resposta = cursor.fetchone()

            if resposta is None:
                print("numero nao encontrado")
                return None

            id_usuario      = resposta[0]
            nome            = resposta[1]
            cpf             = resposta[2]
            email           = resposta[3]
            data_nascimento = resposta[4]
            telefone        = resposta[5]
            status          = resposta[6]
            tipo            = resposta[7]
            print(f"id: {id_usuario} - nome: {nome} - cpf: {cpf} - email: {email} - nascimento: {data_nascimento} - telefone: {telefone} - status: {status} - tipo: {tipo}")
            return resposta

        except Exception as e:
            print(f"Erro ao buscar telefone: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def buscar_por_nome(nome):
        sql = "EXEC P_pesquisaNumeroNome ?"
        valor = (nome,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valor)

            linhas = cursor.fetchall()

            if not linhas:
                print("nenhum telefone encontrado")
                return None

            for linha in linhas:
                id_usuario      = linha[0]
                nome            = linha[1]
                cpf             = linha[2]
                email           = linha[3]
                data_nascimento = linha[4]
                telefone        = linha[5]
                status          = linha[6]
                tipo            = linha[7]
                print(f"id: {id_usuario} - nome: {nome} - cpf: {cpf} - email: {email} - nascimento: {data_nascimento} - telefone: {telefone} - status: {status} - tipo: {tipo}")

            return linhas

        except Exception as e:
            print(f"Erro ao buscar telefone por nome: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def buscar_por_tipo(tipo):
        sql = "EXEC P_pesquisaTelefoneTipo ?"
        valor = (tipo,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valor)

            linhas = cursor.fetchall()

            if not linhas:
                print("nenhum telefone encontrado")
                return None

            for linha in linhas:
                id_usuario      = linha[0]
                nome            = linha[1]
                cpf             = linha[2]
                email           = linha[3]
                data_nascimento = linha[4]
                telefone        = linha[5]
                status          = linha[6]
                tipo            = linha[7]
                print(f"id: {id_usuario} - nome: {nome} - cpf: {cpf} - email: {email} - nascimento: {data_nascimento} - telefone: {telefone} - status: {status} - tipo: {tipo}")

            return linhas

        except Exception as e:
            print(f"Erro ao buscar telefone por tipo: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def buscar_por_status(status):
        sql = "EXEC P_pesquisaTelefonestatus ?"
        valor = (status,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valor)

            linhas = cursor.fetchall()

            if not linhas:
                print("nenhum telefone encontrado")
                return None

            for linha in linhas:
                id_usuario      = linha[0]
                nome            = linha[1]
                cpf             = linha[2]
                email           = linha[3]
                data_nascimento = linha[4]
                telefone        = linha[5]
                status          = linha[6]
                tipo            = linha[7]
                print(f"id: {id_usuario} - nome: {nome} - cpf: {cpf} - email: {email} - nascimento: {data_nascimento} - telefone: {telefone} - status: {status} - tipo: {tipo}")

            return linhas

        except Exception as e:
            print(f"Erro ao buscar telefone por status: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def atualizar_telefone(id_telefone, telefone, tipo):
        sql = "EXEC P_atualizarTelefone ?, ?, ?"
        valores = (id_telefone, telefone, tipo)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            conn.commit()
            return "telefone atualizado com sucesso"

        except Exception as e:
            print(f"Erro ao atualizar telefone: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def atualizar_status(id_telefone, status):
        sql = "EXEC P_atualizarStatusTelefone ?, ?"
        valores = (id_telefone, status)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            conn.commit()
            return "status atualizado com sucesso"

        except Exception as e:
            print(f"Erro ao atualizar status do telefone: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def excluir_telefone(id_telefone):
        sql = "EXEC P_excluirTelefone ?"
        valor = (id_telefone,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valor)
            conn.commit()
            return "telefone excluido com sucesso"

        except Exception as e:
            print(f"Erro ao excluir telefone: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def cadastra_num(tipo,telefone,id_usuariofk):
        sql =  "EXEC P_cadastrarNum ?, ?, ?"
        valores = (tipo,telefone,id_usuariofk)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            conn.commit()
            return "telefone cadastrado com sucesso"
        except Exception as e:
            print(f"Erro ao cadastrar telefone: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()