from classes.Cliente import Cliente
from conexao.Conexao import conexao

class ClienteDAO:

    '''basicamente pra vc fazer uma dao vc guarda a mensagem pro banco em uma varivel
        vc guarda os valores em outra variavel
        vc cria as variveis de conexoa a 
        conn recebe a funcao da conexao com o banco
        cursor vai receber a conn com um metodo cursor() q ja e do python
        esse metodo ja e do pytohn e meio q o entregador da mensagem 
        e o cursor a varivel recebe os valores e executa a conexao
        
        pra vc pegar uma informaçao e como um json mas e uma lista de tuplas
        resposta = cursor.fetchone() vai pegar o primeiro valor vc vai ter q pegar as variaveis q criar e dar o valor de cada indice
        linhas = cursor.fetchall() pega todos os valores vc ria um for informando todas as variaveis e por indice

        pra cadastrrar vc recebe o objeto desempacota em variaveis recebendo os gets e informa essas variveis pro banco 
        
        pra dar um push ou qualquer alteraçaoi no banco vc tenq dar o commit pra comita o dado q foi entregue e como a conbfirmaçao pelo lado do entregador informando q ja fez o envio
        
        conexao sempre feita dentro do try pra nao ocorrer erro de conexao 
        
        basicamente uma api '''
        



    @staticmethod
    def buscar_por_nome(nome):
        sql = "EXEC P_BuscarClientePorNome ?"
        valores = (nome,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)

            linhas = cursor.fetchall()

            if not linhas:
                print("nenhum cliente encontrado")
                return None # se nao tivert nenhuma in formaçaop

            for linha in linhas:
                id_cliente      = linha[0]
                nome            = linha[1]
                cpf             = linha[2]
                email           = linha[3]
                data_nascimento = linha[4]
                data_cadastro   = linha[5]
                status          = linha[6]
                print(f"id: {id_cliente} - nome: {nome} - cpf: {cpf} - email: {email} - nascimento: {data_nascimento} - cadastro: {data_cadastro} - status: {status}")

            return linhas

        except Exception as e:
            print(f"Erro ao buscar cliente por nome: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def buscar_por_email(email):
        sql = "EXEC P_BuscarClienteEmail ?"
        valores = (email,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)

            linhas = cursor.fetchall()

            if not linhas:
                print("nenhum cliente encontrado")
                return None

            for linha in linhas:
                id_cliente      = linha[0]
                nome            = linha[1]
                cpf             = linha[2]
                email           = linha[3]
                data_nascimento = linha[4]
                data_cadastro   = linha[5]
                status          = linha[6]
                print(f"id: {id_cliente} - nome: {nome} - cpf: {cpf} - email: {email} - nascimento: {data_nascimento} - cadastro: {data_cadastro} - status: {status}")

            return linhas

        except Exception as e:
            print(f"Erro ao buscar cliente por email: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def buscar_todos():
        sql = "EXEC P_BuscarClientes"

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql)

            linhas = cursor.fetchall()

            if not linhas:#explicar
                print("nenhum cliente encontrado")
                return None

            for linha in linhas:#explicar
                id_cliente      = linha[0]
                nome            = linha[1]
                cpf             = linha[2]
                email           = linha[3]
                data_nascimento = linha[4]
                data_cadastro   = linha[5]
                status          = linha[6]
                print(f"id: {id_cliente} - nome: {nome} - cpf: {cpf} - email: {email} - nascimento: {data_nascimento} - cadastro: {data_cadastro} - status: {status}")

            return linhas

        except Exception as e:
            print(f"Erro ao buscar clientes: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def buscar_por_cpf(cpf):
        sql = "EXEC P_BuscarClienteCpf ?"
        valores = (cpf,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)

            resposta = cursor.fetchone()

            if resposta is None:
                print("cliente nao encontrado")
                return None

            id_cliente      = resposta[0]
            nome            = resposta[1]
            cpf             = resposta[2]
            email           = resposta[3]
            data_nascimento = resposta[4]
            data_cadastro   = resposta[5]
            status          = resposta[6]
            print(f"id: {id_cliente} - nome: {nome} - cpf: {cpf} - email: {email} - nascimento: {data_nascimento} - cadastro: {data_cadastro} - status: {status}")
            return resposta

        except Exception as e:
            print(f"Erro ao buscar cliente por cpf: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def buscar_por_data_nascimento(data_nascimento):
        sql = "EXEC P_BuscarClientDataNasc ?"
        valores = (data_nascimento,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)

            linhas = cursor.fetchall()

            if not linhas:
                print("nenhum cliente encontrado")
                return None

            for linha in linhas:
                id_cliente      = linha[0]
                nome            = linha[1]
                cpf             = linha[2]
                email           = linha[3]
                data_nascimento = linha[4]
                data_cadastro   = linha[5]
                status          = linha[6]
                print(f"id: {id_cliente} - nome: {nome} - cpf: {cpf} - email: {email} - nascimento: {data_nascimento} - cadastro: {data_cadastro} - status: {status}")

            return linhas

        except Exception as e:
            print(f"Erro ao buscar cliente por data de nascimento: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def atualizar_status(id_cliente, status_cliente):
        sql = "EXEC P_atualizar_estatusbloqueado ?, ?"
        valores = (id_cliente , status_cliente)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            conn.commit()
            return "status atualizado com sucesso"

        except Exception as e:
            print(f"Erro ao atualizar status: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def atualizar_email_senha(id_usuario, email, senha):
        sql = "EXEC P_atualizarEmail ?, ?, ?"
        valores = (id_usuario, email, senha)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            conn.commit()
            return "email e senha atualizados com sucesso"

        except Exception as e:
            print(f"Erro ao atualizar email e senha: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def atualizar_senha(id_usuario, senha):
        sql = "EXEC P_atualizarSenha ?, ?"
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
    def excluir_cliente(id_cliente):
        
        sql = "EXEC P_ExcluirCliente ?"
        valor = (id_cliente,)

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valor)
            conn.commit()
            return "cliente excluido com sucesso"

        except Exception as e:
            print(f"Erro ao excluir cliente: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    @staticmethod
    def cadastro_cliente(cliente, telefone, endereco):

        nome             = cliente.getNome_usuario()
        cpf              = cliente.getCpf()
        email            = cliente.getEmail()
        senha            = cliente.getSenha()
        data_nascimento  = cliente.getData_nascimento()
        numero_residencia = cliente.getNumero_residencia()
        complemento      = cliente.getComplemento()

        numero          = telefone.getTelefone()
        tipo            = telefone.getTipo()

        logradouro      = endereco.getLogradouro()
        cep             = endereco.getCep()
        bairro          = endereco.getBairro()
        cidade          = endereco.getCidade()
        uf              = endereco.getUf()

        sql = "EXEC P_cadastroCliente ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?"
        valores = (
            uf,cidade,
            logradouro, cep, bairro,
            nome, cpf, email, senha, data_nascimento, numero_residencia, complemento,
            numero, tipo
        )

        try:
            conn = conexao.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, valores)
            conn.commit()
            return "CLIENTE cadastrado com sucesso"

        except Exception as e:
            print(f"Erro ao cadastrar funcionário: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()