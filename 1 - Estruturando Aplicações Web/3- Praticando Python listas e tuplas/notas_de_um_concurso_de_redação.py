# Uma escola realizou um concurso de redação, e o próximo passo é organizar as notas dos participantes para definir a ordem de premiação. Para garantir transparência, as notas precisam ser classificadas em ordem crescente, do menor para o maior valor.

# Com base nisso, desenvolva um programa que receba como entrada uma lista contendo as notas de todos os participantes e exiba, ao final, essa lista ordenada em ordem crescente.


# Recebe as notas (exemplo: entrada manual)
notas = list(map(float, input("Digite as notas separadas por espaço: ").split()))

# Ordena em ordem crescente
notas.sort()

# Exibe o resultado
print("Notas em ordem crescente:")
print(notas)