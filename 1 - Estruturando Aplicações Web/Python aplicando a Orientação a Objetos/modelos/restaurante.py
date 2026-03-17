class Restaurante: 
    nome = ''
    categoria = ''
    ativo = False


# instancia inicial 
restaurante_praca = Restaurante()

# 1. atribuir 'Italiana' a categoria
restaurante_praca.categoria = 'Italiana'

# 2. acessar o nome (antes de alterar)
print("Nome inicial:", restaurante_praca.nome)

# 3. Verificar se está ativo ou inativo
if restaurante_praca.ativo:
    print("Restaurante está ativo")
else:
    print("Restaurante está inativo")

# 4. acessar atributo classe  diretamente
categoria = Restaurante.categoria
print("Categoria do restaurante:", categoria)

# 5. Alterar nome para 'Bistrô'
restaurante_praca.nome = 'Bistrô'
print("Nome alterado:", restaurante_praca.nome)

# 6. Criar nova instância restaurante_pizza
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

# 7. Verificar se categoria é 'Fast Food'
if restaurante_pizza.categoria == 'Fast Food':
    print("Categoria do restaurante_pizza é Fast Food")

# 8. Ativar restaurante_pizza
restaurante_pizza.ativo = True

# 9. Imprimir nome e categoria do restaurante_praca
print("Restaurante Praça:")
print("Nome:", restaurante_praca.nome)
print("Categoria:", restaurante_praca.categoria)