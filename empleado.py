from persona import Persona





class Empleado(Persona):
    def __init__(self,lista_empleado =[],depto='random',rut='random',clave='random',nombre='random',cargo='random'):
        super().__init__(rut,clave,nombre,cargo)
        self._lista_empleado = list(lista_empleado)
        self._depto = depto


    def addEmpleado(self):
        #se declaran las variables para pasar su valor como parámetro a la instancia 

        rut = input('ingrese su rut:   ')
        clave = input('ingrese una clave:   ')
        nombre = input('ingrese su nombre:   ')
        cargo = input('ingrese su cargo:   ')
        depto = input('ingrese su depto:   ')


        nuevo_empleado = Empleado([],rut,clave,nombre,cargo,depto)
        
        self._lista_empleado.append(nuevo_empleado)

        



    def mostrarTodos(self):
        num = 0
        for empleado in self._lista_empleado:
            num += 1
            print('empleado número ',num, empleado)

    
    def mostrarLista(self):
        return self._lista_empleado


    def __del__(self):
        print('se eliminó la instancia'.center(30,'-'))







