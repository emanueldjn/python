# Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
class Carro:
    def __init__(self, modelo='', cor='', ano=int):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano


# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
class Restaurante:
    def __init__(self, nome, categoria, ativo, avaliacao, endereco):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.avaliacao = avaliacao
        self.endereco = endereco

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo} | {self.avaliacao} | {self.endereco}'

# Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
# Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
# Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.