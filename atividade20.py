



nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))


media = (nota1 + nota2 + nota3) / 3

if media == 10:
    situacao = "Aprovado com Distinção"
elif media >= 7:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print("Situação do aluno:",situacao)
print("Média alcançada:", media)
