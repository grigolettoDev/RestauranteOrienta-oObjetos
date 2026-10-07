from restaurantes.restaurante import Restaurante

from cardapio.bebida import Bebida
from cardapio.prato import Prato

restaurante_italiano = Restaurante('Grigoletto','Italiano')
restaurante_italiano.recebe_avaliacao('Leonardo',10)
restaurante_italiano.recebe_avaliacao('Sophia',5)
bebida_suco = Bebida('Laranja',20,'Grande')
bebida_suco.aplicar_desconto()
lasanha = Prato('Lasanha',50,'Lasanha com molho Vermelho')
lasanha.aplicar_desconto()
restaurante_italiano.adiciona_no_cardapio(bebida_suco)
restaurante_italiano.adiciona_no_cardapio(lasanha)
#testes 2

def main():
    
    restaurante_italiano.lista_cardapio


if __name__ == '__main__':
    main()