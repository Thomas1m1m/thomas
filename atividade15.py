#Faça um Programa que peça os 3 lados de um triângulo. 
#O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo,
#se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#riângulo Isósceles: quaisquer dois lados iguais;
#riângulo Escaleno: três lados diferentes;

lado1 = int(input("Digite o primeiro lado do triângulo: "))
lado2 = int(input("Digite o segundo lado do triângulo: "))
lado3 = int(input("Digite o terceiro lado do triângulo: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    
    if lado1 == lado2 == lado3:
        tipo = "equilátero"  
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = "isósceles"   
    else:
        tipo = "escaleno"    

    print("Isso é um triângulo", tipo)
else:
    print("Os lados não podem formar um triângulo.")



