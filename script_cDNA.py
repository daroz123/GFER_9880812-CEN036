#!/usr/bin/env python3
import sys 

#Aqui fazer a verificacao sobre quantos args queres receber, que no caso é 5
if len(sys.argv) <= 5: 
    print('argumentos insuficientes')
    sys.exit()
#Verificação se o DNA é str
if sys.argv[1].isdigit():
    print("Argumento para DNA incorreto.")
    sys.exit()
#Verificação se o N1 é inteiro.
if not sys.argv[2].isdigit():
    print("Argumento para n1 incorreto.")
    sys.exit()
#Verificação se o N2 é inteiro.
if not sys.argv[3].isdigit():
    print("Argumento para n2 incorreto.")
    sys.exit()
#Verificação se o N3 é inteiro.
if not sys.argv[4].isdigit():
    print("Argumento para n3 incorreto.")
    sys.exit()
#Verificação se o N4 é inteiro.
if not sys.argv[5].isdigit():
    print("Argumento para n4 incorreto.")
    sys.exit()

#Atribuo os valores passado por parametros a váriaveis locais
DNA = sys.argv[1]
len_DNA = len(DNA)
n1 = int(sys.argv[2])
n2 = int(sys.argv[3])
n3 = int(sys.argv[4])
n4 = int(sys.argv[5])

#Verificações se o tamanho dos n's é maior que o do DNA
if (len_DNA < n1):
    print("Argumento para n1 é maior que o DNA")
    sys.exit()
if (len_DNA < n2):
    print("Argumento para n2 é maior que o DNA")
    sys.exit()
if (len_DNA < n3):
    print("Argumento para n3 é maior que o DNA")
    sys.exit()
if (len_DNA < n4):
    print("Argumento para n4 é maior que o DNA")
    sys.exit()

#Crio as váriaveis CDS_1 e CD_2 com as sequencias corretas
CDS_1 = DNA[n1-1:n2]

CDS_2 = DNA[n3-1:n4]

#Mostro elas na tela para o usuario
print("CDS 1: ",CDS_1)
print("\n")
print("CDS 2: ",CDS_2)
print("\n")


#Verificação de CDS_1
if not CDS_1[:3] == "ATG":
    print("CDS 1 não inicia com ATG")
    sys.exit()

#Verificação de CDS_2
if (not CDS_2[len(CDS_2)-3:] == "TAG") and (not CDS_2[len(CDS_2)-3:] == "TAA") and (not CDS_2[len(CDS_2)-3:] == "TGA"):
    print("CDS 2 não termina com TAG ou TAA ou TGA")
    sys.exit()

#Mostro a sequencia concatenada
print("Sequencia concatenada de CDS 1 e CDS 2: ")
print(CDS_1 + CDS_2)



