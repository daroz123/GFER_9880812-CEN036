#!/usr/bin/env python3
#Recebendo os valores de A e B
a = input("Digite um valor inteiro para A:")
b = input("Digite um valor inteiro para B:")

#Passando ambos valores recebidos de string para inteiro
a_int = int(a)
b_int = int(b)

#Verificando que obdecem a regra (ser maior que 100)
if a_int>100 or b_int>100:
    print("Os valores de A e B, tem que ser MENOR que 100.")
    exit()

#Realizando a conta da hipotenusa ao quadrado
c = (a_int ** 2) + (b_int ** 2)

#Mostrando  o resultado
print("A hipotenusa ao quadrado é:", c)
