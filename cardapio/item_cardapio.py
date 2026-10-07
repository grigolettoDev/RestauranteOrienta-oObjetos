
#Um método abstrato em Python é um método declarado numa classe base que não possui implementação própria (não tem código dentro) e obriga todas as classes filhas (herdeiras) a implementá-lo.
from abc import ABC, abstractmethod

class Cardapio(ABC):
    def __init__(self,nome,preco):
        self._nome = nome
        self._preco = preco
        
# 2. Define o método abstrato com o decorator
    @abstractmethod
    def aplicar_desconto(self):
        """Método obrigatório para todos os itens do cardápio"""
        pass