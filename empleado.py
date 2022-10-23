from persona import Persona

class Empleado(Persona):
    lista_empleado =[]
    def __init__(self,depto='random',rut='random',clave='random',nombre='random',cargo='random'):
        super().__init__(rut,clave,nombre,cargo)
        
        self._depto = depto

        def __str__(self):
            return f' el nombre del empleado es {super()._nombre}'

    #definimos las funciones de set y get

    def getRut(self):
        return self._rut
    def getClave(self):
        return self._clave
    def setClave(self):
        clave = input('ingrese su nueva clave:   ')
        self._clave = clave
    def setNombre(self):
        nombre = input('ingrese su nuevo nombre:   ')
        self._nombre = nombre
    def setCargo(self):
        cargo = input('ingrese su nuevo cargo:   ')
        self._cargo = cargo


    def modificarEmpleado(self):

        opcion = input('ingrese su opción    :   ')
        rut = input("Ingrese el rut del empleado a modificar : ")

        if opcion == '1':
                    
            if (len(self.mostrarLista()) == 0):
                print('no existe ese empleado')
            else:
                for e in self.mostrarLista():
                    if (e.getRut() == rut):
                        e.setClave()
                print('clave modificada!')
        if opcion == '2':
            if (len(self.mostrarLista()) == 0):
                print('no existe ese empleado')
            else:
                for e in self.mostrarLista():
                    if (e.getRut() == rut):
                        e.setNombre()
                print('nombre  modificado!')
        
        if opcion == '3':
            if (len(self.mostrarLista()) == 0):
                print('no existe ese empleado')
            else:
                for e in self.mostrarLista():
                    if (e.getRut() == rut):
                        e.setCargo()
                print('cargo  modificado!')
        
        else:
            print('no existe ese empleado :(')
        





    def addEmpleado(self):
        #se declaran las variables para pasar su valor como parámetro a la instancia 
        # es importante que el orden de los parámetros sean los mismo que fueron establecidos en el constructor

        rut = input('ingrese su rut:   ')
        clave = input('ingrese una clave:   ')
        nombre = input('ingrese su nombre:   ')
        cargo = input('ingrese su cargo:   ')
        depto = input('ingrese su depto:   ')


        nuevo_empleado = Empleado(depto,rut,clave,nombre,cargo)
        
        self.lista_empleado.append(nuevo_empleado)

    def mostrarLista(self):
        return self.lista_empleado

# se declara una variable para contar el número del empleado
    def mostrarTodos(self):
        num = 0
        for empleado in self.lista_empleado:
            num += 1
            print('empleado número ',num, empleado)


    
    def buscarEmpleado(self):
        rut = input("Ingrese el rut del empleado: ")
        if (len(self.mostrarLista()) == 0):
            print('no existe ese empleado')
        else:
            for e in self.mostrarLista():
                if (e.getRut() == rut):
                     print(e)

            
    def subEmpleado(self):
        rut = input("Ingrese el rut del empleado: ")
        if (len(self.mostrarLista()) == 0):
            print('no existe ese empleado')
        else:
            for e in self.mostrarLista():
                if (e.getRut() == rut):
                     self.lista_empleado.remove(e)



        






    def __del__(self):
        print('se eliminó la instancia'.center(30,'-'))








    # def buscarEmpleado(self):
    #     rut = input("Ingrese el rut del empleado: ")
    #     empleado = filter(lambda empleados:self.getRut() == rut,self.lista_empleado )
    #     for cada_empleado in  empleado:
    #         print(cada_empleado)
    #         print(empleado)
    #     print(empleado)
    #     print('si sale esto es por que no funciona ')

    def __str__(self):
        return f"Rut: {self._rut}, Clave: {self._clave}, Nombre: {self._nombre}, Cargo: {self._cargo}"

# emp1 = Empleado('casero','19239872k','no lo se','esteban muñoz','nose')
# emp2 = Empleado('casero','102034252','no lo se','eduardo muñoz','nose')
# emp3 = Empleado('casero','130540945','no lo se','patricia rojas','nose')
# lista = [emp1,emp2,emp3]
# empleados = Empleado()

# empleados.lista_empleado = lista
# print(empleados.lista_empleado)