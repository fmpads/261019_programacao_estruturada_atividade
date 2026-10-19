'''
19/10/26
Faculdade Municipal de Palhoça (FMP)
Tecnologia em Análise e Desenvolvimento de Sistemas
Programação Estruturada
Docente: Daniela Amorim  
Discente: Jean Douglas Toledo Rodrigues Junior (jean.rodrigues@aluno.fmpsc.edu.br)

Lista Laço de Repetição
'''
print(f"Exercício 1. Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e mostrar:")
print(f"a. A menor altura do grupo;")
print(f"b. A maior altura do grupo;")
menorAltura = 0
maiorAltura = 0
for i in range (1, 16):
    altura = float(input(f"Digite a {i}ª altura (em metros): "))
    if (i == 1):
        menorAltura = altura
        maiorAltura = altura
    else:
        if (altura < menorAltura):
            menorAltura = altura
        elif (altura >= maiorAltura):
            maiorAltura = altura
print(f"Maior Altura: ", maiorAltura, " metros")
print(f"Menor Altura: ", menorAltura, " metros")

print(f"\nExercício 2. Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200.")
for i in range(100, 201):
    if i % 2 != 0:
        print(i)

print(f"\nExercício 3. Escreva um algoritmo que leia um valor inicial A e imprima a sequência de valores do cálculo de A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120")
numero = int(input("Digite o número: "))
sentenca = (f"{numero}! = ")
resultado = 1

for i in range (numero, 0, -1):
    resultado = resultado * i
    if i != 1:
        sentenca = sentenca + str(i) + " x "
    else:
        sentenca = sentenca + str(i) + " = " + str(resultado)
print(sentenca)

print(f"\nExercício 4. Escrever um algoritmo que lê 5 valores para a, um de cada vez, e conta quantos destes valores são negativos.")
quantNegativo = 0
for i in range (1, 6):
    a = float(input(f"Digite o {i}º valor de a: "))
    if a < 0:
        quantNegativo = quantNegativo + 1
print(f"A quantidade de números negativos é: ", quantNegativo)

print(f"\nExercício 5. Em uma eleição presidencial existem quatro candidatos. Os votos são informados através de códigos. Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:")
print(f"a. 1,2,3,4 = voto para os respectivos candidatos;")
print(f"a. 1,2,3,4 = voto para os respectivos candidatos;")
print(f"b. 5 = voto nulo;")
print(f"c. 6 = voto em branco;")
print(f"d. Elabore um algoritmo que leia o código do candidato em um voto.")
print(f"Calcule e escreva:")
print(f"e. total de votos para cada candidato;")
print(f"f. total de votos nulos;")
print(f"g. total de votos em branco;")
print(f"Faça um algoritmo para ler pelo menos 100 votos.")
contCad1 = 0
contCad2 = 0
contCad3 = 0
contCad4 = 0
contBranco = 0
contNulo = 0
for i in range(1, 11):
    voto = int(input("Voto: "))
    if voto == 1:
        contCad1 += 1
    elif voto == 2:
        contCad2 += 1
    elif voto == 3:
        contCad3 += 1
    elif voto == 4:
        contCad4 += 1
    elif voto == 6:
        contBranco += 1
    else:
        contNulo += contNulo + 1
print(f"O candidado 1 totalizou: {contCad1} votos.")
print(f"O candidado 2 totalizou: {contCad2} votos.")
print(f"O candidado 3 totalizou: {contCad3} votos.")
print(f"O candidado 4 totalizou: {contCad4} votos.")
print(f"Voto em Branco totalizou: {contBranco} votos.")
print(f"Voto em Nulo totalizou: {contNulo} votos.")

print(f"\nExercício 6. Solicite que o usuário insira seu nome completo e informe quantos caracteres ele possui.")
nome = input("Digite o seu nome completo: ")
quantCaracteres = len(nome)
print(f"Seu nome tem:", quantCaracteres, " caracteres")

print(f"\nExercício 7. Solicite que o usuário insira seu nome completo e apresente apenas o primeiro nome.")
nomeCompleto = input("Digite seu nome completo: ")
primeiroNome = nomeCompleto.split()[0]
print(f"\na. Na vertical")
for letra in primeiroNome:
    print(letra)
print(f"b. Na horizontal")
print(primeiroNome)