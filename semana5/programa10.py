class Alumno: ##crea la clase  alumno
    __nombre = None
    __matricula = None
    __carrera = None
    def setNombre(self,nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre

    def setMatricula(self,matricula):
        self.__matricula = matricula
    def getMatricula(self):
        return self.__matricula

    def setCarrera(self,carrera):
        self.__carrera = carrera
    def getCarrera(self):
        return self.__carrera
dejah = Alumno ()
dejah.setNombre("Kevin")
print(dejah.getNombre())

objeto = Alumno ()
objeto.setMatricula("1722110036")
print(objeto.getMatricula())

objeto = Alumno ()
objeto.setCarrera("Desarrollo de software multiplataforma")
print(objeto.getCarrera())