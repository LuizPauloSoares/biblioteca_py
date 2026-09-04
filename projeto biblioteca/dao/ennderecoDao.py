from conexao.Conexao import conexao
from classes.Endereco import Endereco

class EnderecoDAO:

    @staticmethod
    def atualizar_endereco(id_usuario, logradouro, cep, bairro, cidade):
        sql = "EXEC P_atualizarEndereco ?, ?, ?, ?, ?"
        valores = (id_usuario, logradouro, cep, bairro, cidade)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            conn.commit()
            return "endereco atualizado com sucesso"

        except Exception as e:
            print(f"Erro ao atualizar endereco: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def excluir_endereco(id_endereco):
        sql = "EXEC P_excluirEndereco ?"
        valor = (id_endereco,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valor)
            conn.commit()
            return "endereco excluido com sucesso"

        except Exception as e:
            print(f"Erro ao excluir endereco: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def listar_endereco_usuario(id_usuario):
        sql = "EXEC P_listarEnderecoUsuario ?"
        valor = (id_usuario,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valor)

            linhas = cursor.fetchall()

            if not linhas:
                print("nenhum endereco encontrado")
                return None

            for linha in linhas:
                id_usuario       = linha[0]
                nome             = linha[1]
                numero_residencia = linha[2]
                complemento      = linha[3]
                logradouro       = linha[4]
                cep              = linha[5]
                bairro           = linha[6]
                status_endereco  = linha[7]
                cidade           = linha[8]
                uf               = linha[9]
                estado           = linha[10]
                print(f"id: {id_usuario} - nome: {nome} - numero: {numero_residencia} - complemento: {complemento} - logradouro: {logradouro} - cep: {cep} - bairro: {bairro} - status: {status_endereco} - cidade: {cidade} - uf: {uf} - estado: {estado}")

            return linhas

        except Exception as e:
            print(f"Erro ao listar endereco: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def verificar_cep(cep):
        sql = "EXEC P_verificarCep ?"
        valor = (cep,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valor)

            resposta = cursor.fetchone()

            if resposta is None:
                print("cep nao encontrado")
                return None

            id_endereco     = resposta[0]
            logradouro      = resposta[1]
            cep             = resposta[2]
            bairro          = resposta[3]
            status_endereco = resposta[4]
            cidade          = resposta[5]
            uf              = resposta[6]
            estado          = resposta[7]
            print(f"id: {id_endereco} - logradouro: {logradouro} - cep: {cep} - bairro: {bairro} - status: {status_endereco} - cidade: {cidade} - uf: {uf} - estado: {estado}")
            return resposta

        except Exception as e:
            print(f"Erro ao verificar cep: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def verificar_bairro(bairro):
        sql = "EXEC P_verificarBairro ?"
        valor = (bairro,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valor)

            linhas = cursor.fetchall()

            if not linhas:
                print("bairro nao encontrado")
                return None

            for linha in linhas:
                id_endereco     = linha[0]
                logradouro      = linha[1]
                cep             = linha[2]
                bairro          = linha[3]
                status_endereco = linha[4]
                cidade          = linha[5]
                uf              = linha[6]
                estado          = linha[7]
                print(f"id: {id_endereco} - logradouro: {logradouro} - cep: {cep} - bairro: {bairro} - status: {status_endereco} - cidade: {cidade} - uf: {uf} - estado: {estado}")

            return linhas

        except Exception as e:
            print(f"Erro ao verificar bairro: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def verificar_logradouro(logradouro):
        sql = "EXEC P_verificarLogradouro ?"
        valor = (logradouro,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valor)

            linhas = cursor.fetchall()

            if not linhas:
                print("logradouro nao encontrado")
                return None

            for linha in linhas:
                id_endereco     = linha[0]
                logradouro      = linha[1]
                cep             = linha[2]
                bairro          = linha[3]
                status_endereco = linha[4]
                cidade          = linha[5]
                uf              = linha[6]
                estado          = linha[7]
                print(f"id: {id_endereco} - logradouro: {logradouro} - cep: {cep} - bairro: {bairro} - status: {status_endereco} - cidade: {cidade} - uf: {uf} - estado: {estado}")

            return linhas

        except Exception as e:
            print(f"Erro ao verificar logradouro: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def verificar_uf(uf):
        sql = "EXEC P_verificarUf ?"
        valor = (uf,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valor)

            linhas = cursor.fetchall()

            if not linhas:
                print("uf nao encontrada")
                return None

            for linha in linhas:
                id_endereco     = linha[0]
                logradouro      = linha[1]
                cep             = linha[2]
                bairro          = linha[3]
                status_endereco = linha[4]
                cidade          = linha[5]
                uf              = linha[6]
                estado          = linha[7]
                print(f"id: {id_endereco} - logradouro: {logradouro} - cep: {cep} - bairro: {bairro} - status: {status_endereco} - cidade: {cidade} - uf: {uf} - estado: {estado}")

            return linhas

        except Exception as e:
            print(f"Erro ao verificar uf: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def verificar_cidade(cidade):
        sql = "EXEC P_verificarCidade ?"
        valor = (cidade,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valor)

            linhas = cursor.fetchall()

            if not linhas:
                print("cidade nao encontrada")
                return None

            for linha in linhas:
                id_endereco     = linha[0]
                logradouro      = linha[1]
                cep             = linha[2]
                bairro          = linha[3]
                status_endereco = linha[4]
                cidade          = linha[5]
                uf              = linha[6]
                estado          = linha[7]
                print(f"id: {id_endereco} - logradouro: {logradouro} - cep: {cep} - bairro: {bairro} - status: {status_endereco} - cidade: {cidade} - uf: {uf} - estado: {estado}")

            return linhas

        except Exception as e:
            print(f"Erro ao verificar cidade: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()