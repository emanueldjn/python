class Restaurante:
    # Definindo metodo
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    # Definindo outro método especial
    def __str__(self):
        return f'{self.nome} | {self.categoria}'


    # Método nosso
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'Nome: {restaurante.nome} | Categoria: {restaurante.categoria} | Ativo: {restaurante.ativo}')



# Restaurante 1
restaurante_praca = Restaurante('Praça', 'Gourmet')


# Restaurante 2
restaurante_pizza = Restaurante('Pizza Place', 'Italiana')

Restaurante.listar_restaurantes()