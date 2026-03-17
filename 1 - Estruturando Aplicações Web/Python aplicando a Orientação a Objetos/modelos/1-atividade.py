# Crie uma classe chamada Musica com os seguintes atributos e crie 3 objetos definindo cada atributo..

class Musica:
    nome = ''
    artista = ''
    duracao = int

# Agora podemos definir os objetos:

class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.duracao = 355

print(f'Música: {musica1.nome} - Banda: {musica1.artista} - {musica1.duracao} segundos')