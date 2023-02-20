"""
    Programa8
    Nombre: Citlali Hernandez Perez
    Fecha: 07/02/2023
    Descripción:
    Pruebas de la condición 'if'
"""
print('Programa para imprimir un número mayor')
print()
##datos de  entrada 
n1 = int(input('Ingrese el primer valor:'))
n2 = int(input('Ingrese el segundo valor:'))
print()
##Opción 1
if n1 > n2:
    print(n1)
if n2 > n1:
    print(n2)
if n1 == n2:
    print(None)
##Opción 2
if n2 > n1:
    print(n2)
if n1 > n2:
    print(n1)
if n1 == n2:
    print(None)
