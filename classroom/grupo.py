

from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        lista = []
        for x in kwargs.values():
            lista.append(Asignatura(x))
        if(self._asignaturas is None):
            self._asignaturas = lista
        else:
            self._asignaturas += lista

    def agregarAlumno(self, alumno, lista=None):
        if(lista is not None):
            lista.append(alumno)
            if(self.listadoAlumnos is None):
                self.listadoAlumnos = lista
            else:
                self.listadoAlumnos = self.listadoAlumnos + lista
        else:
            self.listadoAlumnos = [alumno]
            
    def __str__(self):
        return "Grupo de estudiantes: grupo predeterminado"

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
