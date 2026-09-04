import string
from datetime import datetime

from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nome_usuario, cpf, email, senha, data_nascimento, numero_residencia, complemento):
        self.__nome_usuario = nome_usuario 
        self.__cpf = cpf
        self.__email = email
        self.__senha = senha
        self.__data_nascimento = data_nascimento 
        self.__numero_residencia = numero_residencia
        self.__complemento = complemento

    def getNome_usuario(self):
        return self.__nome_usuario 

    def getCpf(self):
        return self.__cpf

    def getEmail(self):
        return self.__email

    def getSenha(self):
        return self.__senha

    def getData_nascimento(self):
        return self.__data_nascimento

    def getNumero_residencia(self):
        return self.__numero_residencia

    def getComplemento(self):
        return self.__complemento

    def setNome_usuario(self, nome_usuario):
        if not nome_usuario.replace(" ","").isalpha():
            raise ValueError("nome de usuario invalido")
        self.__nome_usuario = nome_usuario 

    def setCpf(self, cpf):
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError("CPF inválido")
        self.__cpf = cpf

    def setEmail(self, email):
        if ("@" not in email) or  (".com" not in email) or (email.index("@") >email.index(".")):
            raise ValueError("email  inválido")
        lista_provedores = ["gmail","hotmail","outlook","yahoo","icloud"]
        tem_provedor = any( i in email for i in lista_provedores)
        if tem_provedor:
            self.__email = email
        else:
            raise ValueError("email  inválido")

    def setSenha(self, senha):
        if (len(senha) < 6):
            raise ValueError ("Senha inválida: mínimo 6 caracteres, um número e um caractere especial")
        tem_pontuacao = any(char in string.punctuation for char in senha)
        tem_numero = any(i in string.digits  for i in senha)
        if tem_numero and tem_pontuacao:
            self.__senha = senha
        else:
            raise ValueError ("Senha inválida: mínimo 6 caracteres, um número e um caractere especial")

    def setData_nascimento(self, data_nascimento):
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
        ano_nascimento = data_nascimento.year
        ano_atual = datetime.now().year
        if ano_nascimento == ano_atual:
            raise ValueError("data de nascimento nao pode ser a data atual")
        elif ano_nascimento > ano_atual:
            raise ValueError("data de nascimento nao pode ser maior data atual")
        elif ano_nascimento < (ano_atual - 70):
            raise ValueError("data de nascimento maior q o permitido")
        elif ano_nascimento > (ano_atual - 13):
            raise ValueError("data de nascimento menor q o permitido")
        else:
            self.__data_nascimento = data_nascimento 

    def setNumero_residencia(self, numero_residencia):
        tem_pontuacao = any(char in string.punctuation for char in numero_residencia)
        if tem_pontuacao:
            raise ValueError("numero da residencia invalido")
        else:
            self.__numero_residencia = numero_residencia

    def setComplemento(self, complemento):
        tem_pontuacao = any(char in string.punctuation for char in complemento)
        if tem_pontuacao:
            raise ValueError(" complemento invalido")
        else:
            self.__complemento = complemento

    @abstractmethod
    def exibirInfo(self):
        pass