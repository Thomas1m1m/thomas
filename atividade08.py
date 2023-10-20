# Faça um programa que pergunte o preço de três produtos e informe qual
#  produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input("Digite o preço do primeiro produto: "))
produto2 = float(input("Digite o preço do segundo produto: "))
produto3 = float(input("Digite o preço do terceiro produto: "))

menorValor = min(produto1, produto2, produto3)
maiorValor = max(produto1, produto2, produto3)

print("O produto mais barato é: ", menorValor)
print("O produto mais caro é: ", maiorValor)