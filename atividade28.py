#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
#porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
#Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
#contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

tipo_carne = input("Digite o tipo de carne (File Duplo, Alcatra ou Picanha): ")
quantidade = float(input("Digite a quantidade em Kg: "))

if quantidade <= 5:
    if tipo_carne == "File Duplo":
        preco_por_kg = 4.90
    elif tipo_carne == "Alcatra":
        preco_por_kg = 5.90
    elif tipo_carne == "Picanha":
        preco_por_kg = 6.90
    else:
        print("Tipo de carne inválido.")
        exit()
else:
    if tipo_carne == "File Duplo":
        preco_por_kg = 5.80
    elif tipo_carne == "Alcatra":
        preco_por_kg = 6.80
    elif tipo_carne == "Picanha":
        preco_por_kg = 7.80
    else:
        print("Tipo de carne inválido.")
        exit()

valor_total = quantidade * preco_por_kg
cartao_tabajara = input("A compra será feita no cartão Tabajara? (S/N): ").strip().lower()
if cartao_tabajara == "s":
    desconto = valor_total * 0.05
else:
    desconto = 0
valor_a_pagar = valor_total - desconto

print("\nCUPOM FISCAL")
print(f"Tipo de carne: {tipo_carne}")
print(f"Quantidade: {quantidade} Kg")
print(f"Preço por Kg: R$ {preco_por_kg:.2f}")
print(f"Valor total: R$ {valor_total:.2f}")
print(f"Tipo de pagamento: {'Cartão Tabajara' if cartao_tabajara == 's' else 'Outro'}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")