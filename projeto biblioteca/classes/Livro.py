import string
from datetime import datetime


class Livro:
    def __init__(self, autor, titulo, ano_lancamento, editora, genero, qnt_livro):
        self.__autor          = autor
        self.__titulo         = titulo
        self.__ano_lancamento = ano_lancamento
        self.__editora        = editora  
        self.__genero         = genero    
        self.__qnt_livro      = qnt_livro

    # geters
    def getAutor(self):
        return self.__autor

    def getTitulo(self):
        return self.__titulo

    def getAno_lancamento(self):
        return self.__ano_lancamento

    def getEditora(self):        
        return self.__editora

    def getGenero(self):         
        return self.__genero

    def getQnt_livro(self):
        return self.__qnt_livro

    # seters
    def setAutor(self, autor):
        tem_pontuacao = any(char in string.punctuation for char in autor)
        tem_numero = any(i in string.digits  for i in autor)
        if tem_numero or tem_pontuacao:
            raise ValueError ("nome de altor invalido")
        else:
            self.__autor = autor
        

    def setTitulo(self, titulo):
        titulo = titulo.strip()
        if titulo == "" or not titulo:
            raise ValueError("titulo invalido")
        self.__titulo = titulo

    def setAno_lancamento(self, ano_lancamento):
        ano_atual = datetime.now().year
        if not ano_lancamento.isdigit():
            raise ValueError ("ano de lançamento invalido")
        elif len(ano_lancamento) != 4 or int(ano_lancamento) > ano_atual:
            raise ValueError ("ano de lançamento invalido")
        else:
            self.__ano_lancamento = ano_lancamento

    def setEditora(self, editora): 
        tem_pontuacao = any(char in string.punctuation for char in editora)   
        if tem_pontuacao:
            raise ValueError ("nome de editora invalido")
        self.__editora = editora

    def setGenero(self, genero):  
        tem_pontuacao = any(char in string.punctuation for char in genero)
        tem_numero = any(i in string.digits  for i in genero)
        if tem_numero or tem_pontuacao:
            raise ValueError ("genero invalido")    
        self.__genero = genero

    def setQnt_livro(self, qnt_livro):
        if not qnt_livro.isdigit():
            raise ValueError("tipo de dado invalido")
        if int(qnt_livro) <= 0:
            raise ValueError("quantidade invalida")
        self.__qnt_livro = qnt_livro