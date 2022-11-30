import random 

print("Bem vindo ao jogo de adivinhação")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
pontos = 1000

print("Qual nível de dificuldade você deseja? ")
print("(1):Fácil, (2):Médio, (3):Dificil")

nivel = int(input("Defina um nível: "))

if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 12
else:
    total_de_tentativas = 6     


for rodada in range (1, total_de_tentativas + 1):
    print("Tentativas {} de {} ".format(rodada, total_de_tentativas))
    
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou", chute_str)
    chute = int(chute_str)
    
    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100: ")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabêns você acertou e fez {} pontos ".format(pontos))
        break
    else:
        if(maior):
            print("Você digitou um número maior do que o numero secreto")
        elif(menor):
            print("Você digitou um número menor do que o numero secreto")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        if(maior):
            print("O seu chute foi maior que o número secreto")
            if (rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {}".format(
                    numero_secreto, pontos))
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
            if (rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))

print("Fim do jogo")