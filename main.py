from clase_usuario import Usuario
from clase_accion import Accion
from clase_transaccion import Transaccion
from interfaz import Interfaz


if __name__ == '__main__':

    def documento(id):
        try:
            with open('sesiones.txt', 'r') as f:
                lineas = f.readlines()

            for linea in lineas:
                datos = linea.split(' ')
                if int(datos[0]) == id:
                    nombre_usuario = datos[1]
                    contraseña = datos[2]
                    email = datos[3]
                    dinero = datos[4]
                    return nombre_usuario, contraseña, email, dinero

        except FileNotFoundError:
            with open('sesiones.txt', 'w'):
                pass




    def registro():
        nombre_usuario = input('Ingrese su nombre: ')
        contraseña=input('Ingrese su contraseña: ' )
        email=input('Ingrese su email: ' )
        dinero=input('Ingrese su dinero: ')



        usuario=Usuario(nombre_usuario, contraseña, email, dinero)

    def inicio():
        nombre_usuario = input('Ingrese su nombre: ')
        contraseña = input('Ingrese su contraseña: ')


        usuario = Usuario(nombre_usuario, contraseña, email, dinero)

