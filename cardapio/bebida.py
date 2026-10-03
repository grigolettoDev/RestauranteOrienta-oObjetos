from cardapio.item_cardapio import Cardapio
#Importando a classe mãe que vai servir de Herança para trazer dados que vão ser aplicados para todos

class Bebida(Cardapio):
    #Declaro a classe mãe na classe atual
    def __init__(self,nome,preco,tamanho):
        #Defino que os valores que eu passar vão ser aplicados conforme a classe mãe
        super().__init__(nome,preco)
        self._tamanho = tamanho
        #O atributo de cima é de acordo com a classe atual

    def __str__(self):
        return(f'{self._nome.ljust(25)} | {str(self._preco).ljust(25)} | {self._tamanho.ljust(25)}')