class Endereco:
    def __init__(self, uf, estado, cidade, logradouro, cep, bairro):
        self.__uf = uf
        self.__estado = estado
        self.__cidade = cidade
        self.__logradouro = logradouro
        self.__cep = cep
        self.__bairro = bairro

    def getUf(self):
        return self.__uf

    def getEstado(self):
        return self.__estado

    def getCidade(self):
        return self.__cidade

    def getLogradouro(self):
        return self.__logradouro
        
    def getCep(self):
        return self.__cep
        
    def getBairro(self):
        return self.__bairro

    def setUf(self, uf):
        self.__uf = uf

    def setEstado(self, estado):
        self.__estado = estado

    def setCidade(self, cidade):
        self.__cidade = cidade

    def setLogradouro(self, logradouro):
        self.__logradouro = logradouro

    def setCep(self, cep):
        if len(cep) != 8 or not cep.isdigit():
            raise ValueError("cep invalido")
        self.__cep = cep

    def setBairro(self, bairro):
        self.__bairro = bairro