#Faça um Programa que peça dois números e imprima o maior deles.

n1 = int (input("digite um número inteiro: "))
n2 = int (input("digite outro número inteiro: "))

if n1 > n2:
    print(n1, 'é maior que', n2)

else:
    print(n2, 'é maior que', n1)