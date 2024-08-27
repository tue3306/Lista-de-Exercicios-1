# Exercício 5
import random

opcoes = ["pedra", "papel", "tesoura"]
vitorias_usuario = 0
vitorias_maquina = 0
empates = 0

while True:
    usuario = input("Escolha pedra, papel ou tesoura (ou 'sair' para parar e ver os resultados finais): ").lower()
    if usuario == 'sair':
        break
    if usuario not in opcoes:
        print("Escolha inválida!")
        continue
    
    maquina = random.choice(opcoes)
    print(f"Máquina escolheu: {maquina}")

    if usuario == maquina:
        print("Empate!")
        empates += 1
    elif (usuario == "pedra" and maquina == "tesoura") or \
         (usuario == "tesoura" and maquina == "papel") or \
         (usuario == "papel" and maquina == "pedra"):
        print("Você venceu!")
        vitorias_usuario += 1
    else:
        print("Máquina venceu!")
        vitorias_maquina += 1

print(f"\nResultados finais:\nVitórias do usuário: {vitorias_usuario}\nVitórias da máquina: {vitorias_maquina}\nEmpates: {empates}")


