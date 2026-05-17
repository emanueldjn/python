# Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, marca e modelo. A classe deve ter um atributo protegido _ligado inicializado como False por padrão.
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False  # atributo protegido


    # Construa o Método Especial str: Adicione um método especial str à classe Veiculo que retorna uma mensagem formatada com a marca, modelo e o estado de ligado/desligado do veículo.
    def __str__(self):
        estado = "Ligado" if self._ligado else "Desligado"
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Estado: {estado}"


# Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. No construtor da classe Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro.
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas


    # Implemente o Método Especial str na Classe Filha: Adicione um método especial str à classe Carro que estenda o método da classe pai (Veiculo) e inclua a informação sobre a quantidade de portas do carro.
    def __str__(self):
        return f"{super().__str__()}, Portas: {self.portas}"


# Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual.
class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo


    # Implemente o Método Especial str na Classe Filha (Moto): Adicione um método especial str à classe Moto que estenda o método da classe pai (Veiculo) e inclua a informação sobre o tipo da moto.
    def __str__(self):
        return f"{super().__str__()}, Tipo: {self.tipo}"


# Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.
# (Neste caso, tudo está no mesmo arquivo conforme solicitado)


# Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.
if __name__ == "__main__":

    # Criando instâncias de Carro
    carro1 = Carro("Toyota", "Corolla", 4)
    carro2 = Carro("Honda", "Civic", 4)
    carro3 = Carro("Fiat", "Uno", 2)

    # Criando instâncias de Moto
    moto1 = Moto("Yamaha", "R1", "Esportiva")
    moto2 = Moto("Honda", "CG 160", "Casual")
    moto3 = Moto("Kawasaki", "Ninja", "Esportiva")


    # Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.
    print("=== CARROS ===")
    print(carro1)
    print(carro2)
    print(carro3)

    print("\n=== MOTOS ===")
    print(moto1)
    print(moto2)
    print(moto3)