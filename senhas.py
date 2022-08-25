
class Senhas:
    # tupla = ()
    lista = []
    dic = {}

    def __init__(self, nome, senha):
        self._nome = nome
        self._senha = senha
        # self.tupla = (nome, fone)
        self.lista.append([self._nome, self._senha])
        self.dic = dict(self.lista)


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    # def __str__(self):
    #     return f'{self.dic}'
    def imprime(self):
        for chave, valor in self.dic.items():
            print(chave, ':', valor)




