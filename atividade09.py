#Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 >= numero2 and numero1 >= numero3:
    maior = numero1
    if numero2 >= numero3:
        meio = numero2
        menor = numero3
    else:
        meio = numero3
        menor = numero2
elif numero2 >= numero1 and numero2 >= numero3:
    maior = numero2
    if numero1 >= numero3:
        meio = numero1
        menor = numero3
    else:
        meio = numero3
        menor = numero1
else:
    maior = numero3
    if numero1 >= numero2:
        meio = numero1
        menor = numero2
    else:
        meio = numero2
        menor = numero1


print("Números em ordem decrescente: ", maior, meio, menor)