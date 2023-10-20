#Faça um programa para a leitura de duas notas parciais de um aluno.
#O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

n1 = 0
n2 = 0 
media = 0
soma = 0

n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))

soma = n1 + n2
media = soma / 2

if media >= 7:
    print('aprovado!')
elif media < 7:
    print('reprovado')
else:
    media == 10
    print('aprovado com distinção')



