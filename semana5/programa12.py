"""
    Programa12
    Nombre: Citlali Hernandez Perez
    Fecha: 15/02/2023
    Descripción:
    Clases 
"""
from persona import Persona ## importa la clase Persona del archivo persona.py

class Alumno(Persona): ##crea la clase Alumno que hereda de la clase Persona
    def __init__(self) ->None: ##constructor de la clase
        super().__init__() ##llama al constructor de la clase
        print("Alummno") ##imprime el texto "Alumno"

objeto_alumno = Alumno() ##crea un ovjeto de la clase Alumno