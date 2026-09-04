from classes.usuario import Usuario 

class Funcionario(Usuario):
    def __init__(self, nome_usuario, cpf, email, senha, data_nascimento, numero_residencia, complemento,salario,cargo):
        super().__init__(nome_usuario, cpf, email, senha, data_nascimento, numero_residencia, complemento)
        self.__salario = salario
        self.__cargo = cargo

    def getSalario(self):
        return self.__salario

    def getCargo(self):
        return self.__cargo
    
    def setSalario(self, salario):
        try:
            valor = float(salario)  
        except ValueError:          
            raise ValueError("tipo de dado invalido")
        if valor < 900.00:          
            raise ValueError("valor incorreto")
        self.__salario = valor
        
    def setCargo(self,cargo):
        lista_cargos = ["Bibliotecário", "Atendente", "Gerente", "Administrador", "Estagiário", "Segurança"]
        if not cargo.isalpha():
            raise ValueError("tipo de dado invalido")
        tem_cargo = any(i == cargo for i in lista_cargos )
        if tem_cargo:
            self.__cargo = cargo
        else:
            raise ValueError("cargo invalido")
    
    def exibirInfo(self):
        return f"Funcionario: {self.getNome_usuario()} | Cargo: {self.__cargo} | Salário: {self.__salario}"
