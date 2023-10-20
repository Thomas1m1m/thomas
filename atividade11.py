
#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.


salario = 0

float (salario = input("Digite o salário atual: "))

if salario <= 280.00:
    porcentual = 20
    
elif salario < 280.00 <= 700.00:
    porcentual = 15
    
elif salario < 700.00 <= 1500.00:
 porcentual = 10
 
else: salario < 1500.00
porcentual = 5
    
aumento = porcentual /100
sanovo = aumento * salario

print("seu salario atual é de salario", salario, "reais")
print("seu salario foi de" ,porcentual,"% de aumento")
print("o valor do aumento foi", aumento, )
print("seu novo salário é de", sanovo, "reais")

