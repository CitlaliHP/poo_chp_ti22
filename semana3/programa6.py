"""
    Programa6
    Nombre: Citlali Hernandez Perez
    Fecha: 31/01/2023
    Descripción:
    Área y perímetro de:
    1.- Círculo
    2.-Cuadrado
"""
##Área y perímetro de un círculo
PI=3.1416
print('Primero vamos a calcular el área y perímetro de un círculo')
print()
radio = int(input('Ingrese el valor del radio de un círculo: '))
area_circulo =(PI*radio**2)
perimetro_circulo = (2*PI*radio)
print('El área del círculo con un radio de ', radio, ' es ', area_circulo)
print('El perímetro del círculo con un radio de ', radio, ' es ', perimetro_circulo)
##Área y perímetro de un cuadrado
print()
print('Ahora vamos a calcular el área y perímetro de un cuadrado ')
print()
lado_del_cuadrado = int(input('Ingrese el valor de uno de los lados del cuadrado: '))
area_cuadrado = (lado_del_cuadrado*lado_del_cuadrado)
perimetro_cuadrado = (lado_del_cuadrado*4)
print('El área de un cuadrado con medida en uno de sus lados de ', lado_del_cuadrado, ' es ', area_cuadrado)
print('El perímetro de un cruadrado con medida en uno de sus lados de ', lado_del_cuadrado, ' es ', perimetro_cuadrado)
print('Fin')
