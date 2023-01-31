"""
    Programa5
    Nombre: Citlali Hernandez Perez
    Fecha: 30/01/2023
    Descripción:
    Área y perímetro de triángulos
"""
print("ÁREA DEL TRIÁNGULO")
b = int(input("Ingrese el valor de la base:"))
h = int(input("Ingrese el valor de la altura :"))
l1= int(input("Ingrese el valor de uno de los lados: "))
l2= int(input("Ingrese el valor del lado restante: "))
##ÁREA
area = (b*h)/2
##PARA SACAR EL PERIMETRO
perimetro = b + l1+ l2
print()
print("Perímetro: ", perimetro)
print("Área : ", area)