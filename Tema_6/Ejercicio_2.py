"""En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno
    que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar 
    sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no."""

class Alumno():

    def iniciar(self,nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print('Nombre: ',self.nombre)
        print('Nota: ',self.nota)

    def condicion(self):
        if self.nota >= 6:
            print('El alumno ha aprobado.')
        else:
            print('El alumno ha desaprobado.')

A=Alumno()
A.iniciar('Marco', 6)
A.imprimir()
A.condicion()