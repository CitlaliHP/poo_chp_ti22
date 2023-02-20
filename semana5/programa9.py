"""
    Programa8
    Nombre: Citlali Hernandez Perez
    Fecha: 13/02/2023
    Descripción:
    Clases 'persona'
"""
class Persona: ##crea la clase Profesor que hereda de la clase Persona
    __email = None
    __nombre = None
    def __init__(self):##constructor de la clase
        print("Persona")
    def setNombre(self,nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre
    def setEmail(self,email):
        self.__email = email
    def getEmail(self):
        return self.__email

dejah = Persona ()  ##crea un ovjeto de la clase Profesor 
dejah.setNombre("Dejah") ##crea un ovjeto de la clase Profesor 
print(dejah.getNombre())

objeto = Persona ()  ##crea un ovjeto de la clase Profesor 
objeto.setEmail("Objeto") ##crea un ovjeto de la clase Profesor 
print(objeto.getEmail())