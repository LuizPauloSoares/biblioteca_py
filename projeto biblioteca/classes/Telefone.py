class Telefone:
    def __init__(self, tipo, telefone):
        self.__tipo = tipo
        self.__telefone = telefone

    def getTipo(self):
        return self.__tipo
    
    def getTelefone(self):
        return self.__telefone

    def setTipo(self, tipo):
        lista_tipos = ["Celular","Fixo","Comercial","Recado"]
        tem_tipo = any(i == tipo for i in lista_tipos)
        if tem_tipo:
            self.__tipo = tipo   
        else:
            raise ValueError ("tipo de telefone invalido")

    def setTelefone(self, telefone):
        if not telefone.isdigit():
            raise ValueError("deve conter apenas numeros")
        if self.getTipo() == "Fixo" and len(telefone) != 10:
            raise ValueError ("telefone fixo deve ter 10 digitos")
        if self.getTipo() != "Fixo" and len(telefone) != 11:
            raise ValueError ("telefone  deve ter 11 digitos")
        self.__telefone = telefone