# Em uma carreira de desenvolvimento de software, a prática consistente desempenha um papel fundamental na construção de bases sólidas. Pensando nisso, criamos uma lista de atividades (não obrigatórias) focada em prática para melhorar ainda mais sua experiência de aprendizagem.

# Bora praticar então?


# Desafios
# Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

# Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

# Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

# Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

# Crie uma instância da classe e imprima o valor da propriedade titular.

# Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

# Crie um método de classe para a conta ClienteBanco.




# Crie uma classe chamada ContaBancaria com construtor
class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    # Método __str__
    def __str__(self):
        return f'Titular: {self._titular} | Saldo: {self._saldo}'

    # Método de classe
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

    # Propriedades (forma "pythonica")
    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo


# Criando duas instâncias e imprimindo
conta1 = ContaBancaria("Emanuel", 1000)
conta2 = ContaBancaria("João", 2000)

print(conta1)
print(conta2)


# Testando ativação
ContaBancaria.ativar_conta(conta1)
print("Conta ativa:", conta1.ativo)


# Imprimindo propriedade titular
print("Titular da conta:", conta1.titular)


# Classe ClienteBanco
class ClienteBanco:
    def __init__(self, nome, idade, cpf, email, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self.telefone = telefone

    # Método de classe
    @classmethod
    def criar_cliente_padrao(cls):
        return cls("Cliente Padrão", 0, "00000000000", "email@teste.com", "000000000")


# Instanciando 3 clientes
cliente1 = ClienteBanco("Emanuel", 25, "12345678900", "emanuel@email.com", "11999999999")
cliente2 = ClienteBanco("Maria", 30, "98765432100", "maria@email.com", "11888888888")
cliente3 = ClienteBanco("Carlos", 40, "11122233344", "carlos@email.com", "11777777777")

# Testando método de classe
cliente_padrao = ClienteBanco.criar_cliente_padrao()
print(cliente_padrao.nome)