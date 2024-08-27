# Exercício 4
notas = [6.3, 7.5, 9.2, 5.1, 6.8]
media = sum(notas) / len(notas)
print(f"Média das notas: {media:.2f}")

acima_da_media = [nota for nota in notas if nota > 6]
print(f"Quantidade de notas acima da média (6): {len(acima_da_media)}")
