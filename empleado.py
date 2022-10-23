from persona import Persona






class Empleado(Persona):
    def __init__(self,lista_empleado =[],depto='random',rut='random',clave='random',nombre='random',cargo='random'):
        super().__init__(rut,clave,nombre,cargo)
        self._lista_empleado = list(lista_empleado)
        self._depto = depto

        def __str__(self):
            return f' el nombre del empleado es {super()._nombre}'


    def addEmpleado(self):
        #se declaran las variables para pasar su valor como parámetro a la instancia 

        rut = input('ingrese su rut:   ')
        clave = input('ingrese una clave:   ')
        nombre = input('ingrese su nombre:   ')
        cargo = input('ingrese su cargo:   ')
        depto = input('ingrese su depto:   ')


        nuevo_empleado = Empleado([],rut,clave,nombre,cargo,depto)
        
        self._lista_empleado.append(nuevo_empleado)



    def getRut(self):
        return self._rut

    def mostrarLista(self):
        return self._lista_empleado

#pasamos como  parámetro una instancia que está declarada como variable en el main
   # def buscarEmpleado(self):
    #    while True:
     #       rut = input('ingrese el rut del empleado a buscar :    ')
      #      for empleado in self.mostrarLista():
       #         if  rut in empleado.getRut()  :
        #            print('existe el empleado!')
         #           print(f' el empleado es {empleado} ' )
          #          
           #     else:
            #        print('No existe, busque otro!')

    # def buscarEmpleado(self):
    #     rut = input('ingrese el rut del empleado a buscar :    ')

    #     for empleado in self.mostrarLista():
    #         if rut == self.getRut():
    #             print('existe el empleado!')
    #             print(f' el empleado es {empleado} ' )
    #         else:
    #             print('no hay nada aquí')
    #             self.buscarEmpleado()




    
            
            


# se declara una variable para contar el número del empleado
    def mostrarTodos(self):
        num = 0
        for empleado in self._lista_empleado:
            num += 1
            print('empleado número ',num, empleado)

# def buscarEmpleado(self):
#     rut = input('ingrese el rut del empleado a buscar :    ')
#     for empleado in self.mostrarLista():
#         if rut == self.getRut():
#             print('existe el empleado!')
#             print(f' el empleado es {empleado} ' )
#         else:
#             print('no hay nada aquí')


    # def buscarEmpleado(self):
    #     rut = input('ingrese el rut del empleado a buscar :    ')
    #     if (len(self._lista_empleado) == 0):
    #         return print('no se encuentra el empleado :(')
    #     else:
    #         for e in self._lista_empleado:
    #             if (e.getRut() == rut):
    #                 return e
    #         return False
    
    def buscarEmpleado(self):
        rut = input('ingrese el rut del empleado a buscar :    ')
        try:
            elemento = self.mostrarLista().index(rut)
            print(self.mostrarLista()[elemento])
            
        except ValueError:
            print('Ese empleado no existe :(')
        






    def __del__(self):
        print('se eliminó la instancia'.center(30,'-'))










