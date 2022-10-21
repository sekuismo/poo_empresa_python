from empleado import Empleado

from administrador import Admin
import time

# se almacenan las instancias en variables 
admin_defecto = Admin()
empleados = []
nuevo_empleado =Empleado()


def ayuda():
    nombre = input('Ingresa tu nombre')
    print(f'lo siento {nombre} No podemos ayudarte :(')






#la instancia solamente vive mientras la función esté ejecutada 
#para que no se elimine la instancia es importante que todo el cuerpo de la función viva dentro de un ciclo While true

def subMenu():
    while True:
        time.sleep(0.1)
        print('Bienvenido a la empresa'.center(100,'-'),'\n')
        time.sleep(0.1)
        print('Opción 1 Administrador'.center(100,'-'),'\n')
        time.sleep(0.1)
        print('Opción 2 Empleado'.center(100,'-'),'\n')
        time.sleep(0.1)
        print('Opción 3 ayuda'.center(100,'-'),'\n')
        time.sleep(0.1)
        print('Opción 4 salir'.center(100,'-'),'\n')
        time.sleep(0.1)
        
        inicio_sesion = input('ingrese aquí :    ')
        if inicio_sesion == '1':
            cont_1 = input('ingrese contraseña 1  :    ')
            cont_2 = input('ingrese contraseña 2  :    ')
            cont_3 = input('Digite su rut         :    ')
            if cont_1 == admin_defecto.getAcceso() and cont_2 == admin_defecto.getAcceso2() and cont_3 == admin_defecto.getRut():

                print('Acceso concedido!'.center(100,'-'))

                while True:
                
                    time.sleep(0.1)
                    print('Bienvenido a la empresa'.center(100,'-'),'\n')
                    time.sleep(0.1)
                    print('Opción 1 Administrador'.center(100,'-'),'\n')
                    time.sleep(0.1)
                    print('Opción 2 Empleado'.center(100,'-'),'\n')
                    time.sleep(0.1)
                    print('Opción 3 ayuda'.center(100,'-'),'\n')
                    time.sleep(0.1)
                    print('Opción 4 salir'.center(100,'-'),'\n')
                    time.sleep(0.1)
                    op1 = input('ingreso :    ')
        #Submenú
                    if op1 == '1':
                        print('no hay nada aquí aún')
                    if op1 == '2':

                        print('Bienvenido al submenú empleado'.center(100,'-'),'\n')
                        time.sleep(0.1)
                        print('Opción 1 Ingresar empleado'.center(100,'-'),'\n')
                        time.sleep(0.1)
                        print('Opción 2 Eliminar el último empleado ingresado'.center(100,'-'),'\n')
                        time.sleep(0.1)
                        print('Opción 3 Modificar empleado'.center(100,'-'),'\n')
                        time.sleep(0.1)
                        print('Opción 4 Buscar empleado'.center(100,'-'),'\n')
                        time.sleep(0.1)
                        print('Opción 5 Mostrar empleado'.center(100,'-'),'\n')
                        time.sleep(0.1)
                        print('Opción 6 Volver al menú principal'.center(100,'-'),'\n')
                        time.sleep(0.2)
                    
                        op2 = input('ingreso :    ')
                        
                    
                        if op2 == '1':
                            nuevo_empleado.addEmpleado()
                        if op2 == '2':
                            nuevo_empleado.mostrarLista().pop()
                            print('empleado eliminado!')
                        if op2 == '3':
        #Segundo submenú
                            print('Bienvenido al  tercer submenú '.center(100,'-'),'\n')
                            time.sleep(0.1)
                            print('Opción 1 Modificar clave '.center(100,'-'),'\n')
                            time.sleep(0.1)
                            print('Opción 2 Modificar nombre'.center(100,'-'),'\n')
                            time.sleep(0.1)
                            print('Opción 3 Modificar cargo'.center(100,'-'),'\n')
                            time.sleep(0.1)
                            print('Opción 4 Volver al menú'.center(100,'-'),'\n')
                            time.sleep(0.1)

                            op3 = input('ingreso :    ')

                            if op3 == '1':
                                print('no hay nada aquí aún ')
                            elif op3 == '2':
                                print('no hay nada aquí ahora')
                            elif op3 == '3':
                                print('nada aquí por ahora')
                            elif op3 == '4':
                                print('volvemos al inicio! ')
                        
                        
                        if op2 == '4':
                            
                            
                            nuevo_empleado.buscarEmpleado(nuevo_empleado.mostrarLista())

                        if op2 == '5':
                            nuevo_empleado.mostrarTodos()

                        if op2 == '6':
                            pass

                    if op1 == '3':
                        ayuda()
                    if op1 == '4':
                        break
                #    else:
                 #       print('opción inválida!. \n ingrese otra!')
                        
        if inicio_sesion == '2':
            print('Acceso Denegado!')
        if inicio_sesion == '3':
            ayuda()
        if inicio_sesion == '4':
            break
        

subMenu()