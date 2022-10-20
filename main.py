from empleado import Empleado
from persona import Persona
import time



empleados = []
nuevo_empleado =Empleado()

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
            print('Opción 3 Modificar empleado (salir por ahora)'.center(100,'-'),'\n')
            time.sleep(0.1)
            print('Opción 4 Buscar empleado'.center(100,'-'),'\n')
            time.sleep(0.1)
            print('Opción 5 Mostrar empleado'.center(100,'-'),'\n')
            time.sleep(0.1)
            print('Opción 6 Volver al menú principal'.center(100,'-'),'\n')
            time.sleep(0.2)
            
            op2 = input('ingreso :    ')
            print(' \r')
            
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
                    print('no hay nada aquí ahora :(')
                elif op3 == '4':
                    print('volvemos al inicio! ')
                
                
            if op2 == '4':
                print('no hay nada aún aquí :(')
            if op2 == '5':
                nuevo_empleado.mostrarTodos()
            if op2 == '6':
                pass

        if op1 == '3':
            print('AYUDA YO TAMPOCO SE QUE HACER CON MI VIDA :(')
        if op1 == '4':
            break
        else:
            print('opción inválida!. \n ingrese otra!')
                


subMenu()