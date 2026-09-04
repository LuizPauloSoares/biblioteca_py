from classes.usuario import Usuario  

class Cliente(Usuario):
    def __init__(self, nome_usuario, cpf, email, senha, data_nascimento, numero_residencia, complemento):
        super().__init__(nome_usuario, cpf, email, senha, data_nascimento, numero_residencia, complemento)

    def exibirInfo(self):
        return f"Cliente: {self.getNome_usuario()} | CPF: {self.getCpf()} "