'''
26/10/26
Faculdade Municipal de Palhoça (FMP)
Tecnologia em Análise e Desenvolvimento de Sistemas
Programação Estruturada
Docente: Daniela Amorim  
Discente: Jean Douglas Toledo Rodrigues Junior (jean.rodrigues@aluno.fmpsc.edu.br)

EAD - Lista 2 - Laço de Repetição
'''
print("Exercício 1. Escrever um algoritmo que leia um número n que indica quantos valores devem ser lidos a seguir.")
print("Para cada número lido, mostre uma tabela contendo o valor lido e o fatorial deste valor.\n")

quantidade = int(input("Quantos números deseja digitar? "))
lista = []

for i in range(quantidade):
    numero_digitado = int(input("Digite o {i}º número: "))
    lista.append(numero_digitado)

print(f"\nLista de números: {lista}")
print("\n--- Tabela de Fatoriais ---")

for num in lista:
    resultado = 1
    sentenca = f"{num}! = "
    
    if num == 0:
        sentenca += "1 = 1"
    else:
        for k in range(num, 0, -1):
            resultado *= k
            if k != 1:
                sentenca += f"{k} x "
            else:
                sentenca += f"{k} = {resultado}"
                
    print(sentenca)

print(f"Exercício 2. Escrever um algoritmo que leia uma quantidade de números que deve ser lidos e conte quantos deles estão nos seguintes intervalos: [0,25], [26,50], [51,75] e [76,100].")
quantidade = int(input("Quantos números deseja digitar? "))
lista = []

for i in range(quantidade):
    numero_digitado = int(input("Digite o {i}º número: "))
    lista.append(numero_digitado)

print(f"\nLista de números: {lista}")

if num < 0:
    print(f"O número deve ser positivo")
else:
    somaIntervalo1 = 0
    somaIntervalo2 = 0
    somaIntervalo3 = 0
    somaIntervalo4 = 0
    for num in lista:
        if num >= 0 or num <= 25:
            somaIntervalo1 += 1
        elif num > 25 or num <= 50:
            somaIntervalo2 += 1
        elif num >51 or num <= 75:
            somaIntervalo3 += 1
        else:
            somaIntervalo4 += 1
print(f"Intervalo 1 [0,25]: {somaIntervalo1}")
print(f"Intervalo 2 [26,50]: {somaIntervalo2}")
print(f"Intervalo 3 [51,75]: {somaIntervalo3}")
print(f"Intervalo 4 [76,100]: {somaIntervalo4}")
'''
print(f"3. Faça um algoritmo que leia 10 números inteiros e calcule o somatório dos números negativos.")

print(f"4. Chico tem 1,50m e cresce 2 centímetros por ano, enquanto Juca tem 1,10m e cresce 3 centímetros por ano.")
print(f"Construir um algoritmo que calcule e imprima quantos anos serão necessários para que Juca seja maior que Chico.")

print(f"5. Faça um algoritmo que leia vários números e informe quantos desses números entre 100 e 200 foram digitados.")
print(f"Quando o valor 0 (zero) for lido o algoritmo deverá cessar sua execução.")

print(f"6. Uma rainha requisitou os serviços de um monge, o qual exigiu o pagamento em grãos de trigo da seguinte maneira:")
print(f"- os grãos de trigo seriam dispostos em um tabuleiro de xadrez, de tal forma que a primeira casa do tabuleiro tivesse um grão, e as casas seguintes o dobro da anterior.")
print(f"Construa um algoritmo que calcule quantos grãos de trigo a Rainha deverá pagar ao monge.")
print(f"Um tabuleiro tem 64 casas.")

print(f"7. Construa um algoritmo que leia uma quantidade indeterminada de números inteiros positivos e identifique qual foi o maior número digitado.")
print(f"O final da série de números digitada deve ser indicado pela entrada de –1.")
'''