def contar_vogais(texto):
    vogais = "aeiou"
    qtd = 0

    for letra in texto.lower():
        if letra in vogais:
            qtd += 1
    
    return qtd

texto = input("Digite um texto: ")

print(f"O texto contém {contar_vogais(texto)} vogais")

