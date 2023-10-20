#Faça um Programa que leia um número e exiba o dia correspondente da semana.
#(1-Domingo, 2- Segunda, etc.)
#, se digitar outro valor deve aparecer valor inválido.

numero = int(input("digite um número de 1 a 7, por favor: "))

if numero == 1:
    dia = "Domingo"

elif numero == 2:
    dia = "Segunda"

elif numero == 3:
    dia = "terça"

elif numero == 4:
    dia = "quarta"

elif numero == 5:
    dia = "quinta"

elif numero == 6:
    dia = "Sexta"

elif numero == 7:
    dia = "Sábado"

else:
    dia = "valor inválido"


    print("hoje é" ,dia)


