from restaurantes.avaliacao import Avaliacao
from cardapio.prato import Prato
from cardapio.bebida import Bebida
from cardapio.item_cardapio import Cardapio




class Restaurante:

    #Capitalize deixa apenas a primeira letra da frase em maiuscula já o Tittle deixa de cada palavra
    restaurantes = []
    def __init__(self,nome,tipo):
        self._nome = nome.capitalize()
        self._tipo = tipo.capitalize()
        """self._status = False - Serve para eu indicar que é um atributo, privado
        o usuário consegue mexer no valor, mas é uma boa prática deixar como privado
        """
        self._status = False
        Restaurante.restaurantes.append(self)
        self._avaliacao = []
        self._cardapio = []
    #Ativan
    # do restaurante
    def alterna_estado(self):
        self._status = not self._status

    @classmethod
    # O @classmethod é usado quando se quer utilizar mais de um objeto da mesma classe
    def lista_restaurantes(cls):
        print(f"{'Restaurante'.ljust(25)} | {'Tipo'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}")
        for restaurante in Restaurante.restaurantes:
            print(restaurante)

    # Define o que o print() deve exibir
    def __str__(self):
        return f"{self._nome.ljust(25)} | {self._tipo.ljust(25)} | {str(self.media_nota).ljust(25)} | {self._status}"


    #'Permite eu modificar o valor de um atributo'
    @property

    def status(self):
        return '☑' if self._status else '☒'

    def recebe_avaliacao(self,cliente,nota):
        avaliacao = Avaliacao(cliente,nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_nota(self):
        if not self._avaliacao:
            return 'Sem Avaliação'
        else:
# O for da maneira abaixo sempre vai entrar no atributo _nota do objeto após passar por todas avaliações
            soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            media = round(soma_notas/len(self._avaliacao),1)
            if media > 5:
                media = round(media/2,1)
            return media
        
    
    def adiciona_no_cardapio(self,item):
        if isinstance(item,Cardapio):  #Se for uma instância de Cardapio ou se for uma filha de Cardapio
            self._cardapio.append(item)
        

    @property
    def lista_cardapio(self):
        print(f"Cardapio do Restaurante {self._nome}\n")       
        for i, item in enumerate(self._cardapio,start=1):
            #hasattr verifica se tem o atributo
            mensagem = f'{i}. Nome: {item._nome} | Preço R$: {item._preco} | {"Tamanho: " + item._tamanho if hasattr(item,"_tamanho") else "Descrição: " +  item._descricao}'
            print(mensagem)

    











    