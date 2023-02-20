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
##PI es una constante
PI=3.1416
print('Primero vamos a calcular el área y perímetro de un círculo') #imprime texto 
print() #deja un espacio entre lineas 
radio = int(input('Ingrese el valor del radio de un círculo: ')) #te pide ingresar un valor 
area_circulo =(PI*radio**2) #realiza una operación
perimetro_circulo = (2*PI*radio) #realiza una operación 
print('El área del círculo con un radio de ', radio, ' es ', area_circulo) #imprime el resultado de la operación area_circulo
print('El perímetro del círculo con un radio de ', radio, ' es ', perimetro_circulo) #imprime el resultado de la operación perimetro_circulo 
##Área y perímetro de un cuadrado
print() #deja un espacio entre lineas
print('Ahora vamos a calcular el área y perímetro de un cuadrado ')
print() #deja un espacio entre lineas 
lado_del_cuadrado = int(input('Ingrese el valor de uno de los lados del cuadrado: '))#te pide ingresar un valor 
area_cuadrado = (lado_del_cuadrado*lado_del_cuadrado) #realiza una operación 
perimetro_cuadrado = (lado_del_cuadrado*4) #realiza una operación 
print('El área de un cuadrado con medida en uno de sus lados de ', lado_del_cuadrado, ' es ', area_cuadrado) #imprime el resultado de la operación area_cuadrado
print('El perímetro de un cruadrado con medida en uno de sus lados de ', lado_del_cuadrado, ' es ', perimetro_cuadrado) #imprime el resultado de la operación perimetro_circulo
print('Fin')
