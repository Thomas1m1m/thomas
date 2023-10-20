#Faça um Programa que leia três números e mostre o maior e o menor deles.
maior = 0
menor = 0
n1 = int (input('digite o primeiro número:'))
n2 = int (input('digite o segundo número:'))
n3 = int (input('digite o terceiro número:'))


if n1 > n2 and n1 > n3:
        maior = n1
elif n2 > n1 and n2 > n3:
        maior = n2
elif n3 > n2 and n3 > n1:
        maior = n3
        print(maior,'é o maior número')

if n1 < n2 and n1 < n3:
        menor = n1
elif n2 < n1 and n2 < n3:
        menor = n2
elif n3 < n2 and n3 < n1:
        menor = n3
print(menor,'é o menor número')

