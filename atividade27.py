#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
#receberá ainda um desconto de 10% sobre este total. 
#Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.


quantidade_morangos = float(input("Digite a quantidade de morangos (em Kg): "))
quantidade_macas = float(input("Digite a quantidade de maçãs (em Kg): "))

if quantidade_morangos <= 5:
    preco_morangos = 2.50
else:
    preco_morangos = 2.20

if quantidade_macas <= 5:
    preco_macas = 1.80
else:
    preco_macas = 1.50

valor_total = (quantidade_morangos * preco_morangos) + (quantidade_macas * preco_macas)

if quantidade_morangos + quantidade_macas > 8 or valor_total > 25.00:
    desconto = valor_total * 0.10
else:
    desconto = 0

valor_a_pagar = valor_total - desconto
print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")