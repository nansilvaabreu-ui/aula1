# Crie um algoritimo que leia 3 valores (lados de um triângulo)
# Determine se formam um troangulo, e se formar verifique
# se é um equilátero, iósosceles ou escaleno.
 
lado1 = float (input ("Digite o valor do lado 1: "))
lado2 = float (input ("Digite o valor do lado 2: "))
lado3 = float (input ("Digite o valor do lado 3: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Os três lados formam um triângulo!")

    if lado1 == lado2 and lado2 == lado3:
        print("O triângulo é equilátero.")

    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo é isósceles.")

    else:
        print("O triângulo é escaleno.")

else:
    print("Os três lados não formam um triângulo.")




