class Produto:
    def __init__(self, nome, preco, validade,fabricante,descricao):
        self.__nome = nome
        self.__preco = preco
        self.__validade = validade
        self.__fabricante = fabricante
        self.__descricao = descricao

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @property
    def validade(self):
        return self.__validade

    @property
    def fabricante(self):
        return self.__fabricante

    @property 
    def descricao(self):
        return self.__descricao
    