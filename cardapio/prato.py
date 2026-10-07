from cardapio.item_cardapio import Cardapio

class Prato(Cardapio):
    def __init__(self,nome,preco,descricao):
        super().__init__(nome,preco)
        self._descricao = descricao
    def __str__(self):
        return(f'{self._nome.ljust(25)} | {str(self._preco).ljust(25)} | {self._descricao.ljust(25)}')

    def aplicar_desconto(self):
        desconto = 0.10
        self._preco -= (self._preco*desconto)