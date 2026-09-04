from conexao.Conexao import conexao
from classes.Funcionario import Funcionario

class FuncionarioDAO:

    @staticmethod
    def buscar_funcionario(id_funcionario):
        sql = "EXEC P_buscarFuncionario ?"
        valor = (id_funcionario,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valor)

            resposta = cursor.fetchone()

            if resposta is None:
                print("funcionario nao encontrado")
                return None

            nome           = resposta[0]
            cpf            = resposta[1]
            email          = resposta[2]
            data_nascimento = resposta[3]
            matricula      = resposta[4]
            cargo          = resposta[5]
            salario        = resposta[6]
            print(f"matricula: {matricula} - nome: {nome} - cpf: {cpf} - nascimento: {data_nascimento} - email: {email} - cargo: {cargo} - salario: {salario}")
            return resposta

        except Exception as e:
            print(f"Erro ao buscar funcionario: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def buscar_funcionarios():
        sql = "EXEC P_buscarFuncionarios"

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql)

            linhas = cursor.fetchall()

            if not linhas:
                print("nenhum funcionario encontrado")
                return None

            for linha in linhas:
                nome           = linha[0]
                cpf            = linha[1]
                email          = linha[2]
                data_nascimento = linha[3]
                matricula      = linha[4]
                cargo          = linha[5]
                print(f"matricula: {matricula} - nome: {nome} - cpf: {cpf} - nascimento: {data_nascimento} - email: {email} - cargo: {cargo}")

            return linhas

        except Exception as e:
            print(f"Erro ao buscar funcionarios: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def buscar_por_nome(nome):
        sql = "EXEC P_BuscarFuncionarioPorNome ?"
        valor = (nome,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valor)

            linhas = cursor.fetchall()

            if not linhas:
                print("nenhum funcionario encontrado")
                return None

            for linha in linhas:
                nome           = linha[0]
                cpf            = linha[1]
                email          = linha[2]
                data_nascimento = linha[3]
                matricula      = linha[4]
                cargo          = linha[5]
                print(f"matricula: {matricula} - nome: {nome} - cpf: {cpf} - nascimento: {data_nascimento} - email: {email} - cargo: {cargo}")

            return linhas

        except Exception as e:
            print(f"Erro ao buscar funcionario por nome: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def buscar_por_cargo(cargo):
        sql = "EXEC P_buscarFuncionarioPorCargo ?"
        valor = (cargo,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valor)

            linhas = cursor.fetchall()

            if not linhas:
                print("nenhum funcionario encontrado")
                return None

            for linha in linhas:
                nome           = linha[0]
                cpf            = linha[1]
                email          = linha[2]
                data_nascimento = linha[3]
                matricula      = linha[4]
                cargo          = linha[5]
                salario        = linha[6]
                print(f"matricula: {matricula} - nome: {nome} - cpf: {cpf} - nascimento: {data_nascimento} - email: {email} - cargo: {cargo} - salario: {salario}")

            return linhas

        except Exception as e:
            print(f"Erro ao buscar funcionario por cargo: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def buscar_por_email(email):
        sql = "EXEC P_BuscarFuncionarioEmail ?"
        valor = (email,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valor)

            linhas = cursor.fetchall()

            if not linhas:
                print("nenhum funcionario encontrado")
                return None

            for linha in linhas:
                nome           = linha[0]
                cpf            = linha[1]
                email          = linha[2]
                data_nascimento = linha[3]
                matricula      = linha[4]
                cargo          = linha[5]
                salario        = linha[6]
                print(f"matricula: {matricula} - nome: {nome} - cpf: {cpf} - nascimento: {data_nascimento} - email: {email} - cargo: {cargo} - salario: {salario}")

            return linhas

        except Exception as e:
            print(f"Erro ao buscar funcionario por email: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def buscar_por_cpf(cpf):
        sql = "EXEC P_BuscarFuncionarioCpf ?"
        valor = (cpf,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valor)

            resposta = cursor.fetchone()

            if resposta is None:
                print("funcionario nao encontrado")
                return None

            nome           = resposta[0]
            cpf            = resposta[1]
            email          = resposta[2]
            data_nascimento = resposta[3]
            matricula      = resposta[4]
            cargo          = resposta[5]
            salario        = resposta[6]
            print(f"matricula: {matricula} - nome: {nome} - cpf: {cpf} - nascimento: {data_nascimento} - email: {email} - cargo: {cargo} - salario: {salario}")
            return resposta

        except Exception as e:
            print(f"Erro ao buscar funcionario por cpf: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def buscar_por_data_nascimento(data_nascimento):
        sql = "EXEC P_BuscarFuncionarioDataNasc ?"
        valor = (data_nascimento,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valor)

            linhas = cursor.fetchall()

            if not linhas:
                print("nenhum funcionario encontrado")
                return None

            for linha in linhas:
                nome           = linha[0]
                cpf            = linha[1]
                email          = linha[2]
                data_nascimento = linha[3]
                matricula      = linha[4]
                cargo          = linha[5]
                salario        = linha[6]
                print(f"matricula: {matricula} - nome: {nome} - cpf: {cpf} - nascimento: {data_nascimento} - email: {email} - cargo: {cargo} - salario: {salario}")

            return linhas

        except Exception as e:
            print(f"Erro ao buscar funcionario por data de nascimento: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def aumento(id_funcionario, salario):
        sql = "EXEC P_aumento ?, ?"
        valores = (salario, id_funcionario)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            conn.commit()
            return "aumento realizado com sucesso"

        except Exception as e:
            print(f"Erro ao realizar aumento: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def promocao(id_funcionario, salario, cargo):
        sql = "EXEC P_promocao ?, ?, ?"
        valores = (salario, id_funcionario, cargo)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            conn.commit()
            return "promocao realizada com sucesso"

        except Exception as e:
            print(f"Erro ao realizar promocao: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def atualizar_senha(id_usuario, senha):
        sql = "EXEC P_atualizarSenhaFuncionario ?, ?"
        valores = (id_usuario, senha)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            conn.commit()
            return "senha atualizada com sucesso"

        except Exception as e:
            print(f"Erro ao atualizar senha: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def atualizar_email(id_usuario, email, senha):
        sql = "EXEC P_atualizarEmailFuncionario ?, ?, ?"
        valores = (id_usuario, email, senha)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            conn.commit()
            return "email atualizado com sucesso"

        except Exception as e:
            print(f"Erro ao atualizar email: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def excluir_funcionario(id_funcionario):

        sql = "EXEC P_excluirFuncionario ?"
        valor = (id_funcionario,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valor)
            conn.commit()
            return "funcionario excluido com sucesso"

        except Exception as e:
            print(f"Erro ao excluir funcionario: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def cadastroFuncionario(funcionario, telefone, endereco):
        cargo            = funcionario.getCargo()
        salario          = funcionario.getSalario()
        nome             = funcionario.getNome_usuario()
        cpf              = funcionario.getCpf()
        email            = funcionario.getEmail()
        senha            = funcionario.getSenha()
        data_nascimento  = funcionario.getData_nascimento()
        numero_residencia = funcionario.getNumero_residencia()
        complemento      = funcionario.getComplemento()

        numero          = telefone.getTelefone()
        tipo            = telefone.getTipo()

        logradouro      = endereco.getLogradouro()
        cep             = endereco.getCep()
        bairro          = endereco.getBairro()
        cidade          = endereco.getCidade()
        uf              = endereco.getUf()

        sql = "EXEC P_cadastroFuncionario ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?"
        valores = (
            uf,cidade,
            logradouro, cep, bairro,
            nome, cpf, email, senha, data_nascimento, numero_residencia, complemento,
            numero, tipo, 
            cargo, salario
        )

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            conn.commit()
            return "Funcionário cadastrado com sucesso"

        except Exception as e:
            print(f"Erro ao cadastrar funcionário: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()