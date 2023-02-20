"""
    Programa13
    Nombre: Citlali Hernandez Perez
    Fecha: 15/02/2023
    Descripción:
    Clases 
"""
from persona import Persona ## importa la clase Persona del archivo persona.py

class Profesor(Persona): ##crea la clase Profesor que hereda de la clase Persona
    def __init__(self) ->None: ##constructor de la clase
        super().__init__() ##llama al constructor de la clase
        print("Profesor") ##imprime el texto "Profesor"

objeto_profesor = Profesor() ##crea un ovjeto de la clase Profesor 