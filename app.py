from restaurantes.restaurante import Restaurante

from cardapio.bebida import Bebida
from cardapio.prato import Prato

restaurante_italiano = Restaurante('Grigoletto','Italiano')
restaurante_italiano.recebe_avaliacao('Leonardo',10)
restaurante_italiano.recebe_avaliacao('Sophia',5)
restaurante_italiano.recebe_prato('Lasanha',25,'Massa com queijo molho branco e carne moída')
restaurante_italiano.recebe_bebida('Coca-Cola',10,'Pequeno')

#testes

def main():
    
    Restaurante.lista_restaurantes()


if __name__ == '__main__':
    main()