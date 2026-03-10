from clase_usuario import Usuario
from clase_accion import Accion
from clase_transaccion import Transaccion
from interfaz import Interfaz


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


def registro(usuarios):
    run = True
    while run:
        run = False
        nombre_usuario = input('Ingrese su nombre: ')
        contraseña = input('Ingrese su contraseña: ')
        email = input('Ingrese su email: ')
        dinero = int(input('Ingrese su dinero: '))

        for usuario in usuarios:
            if usuario.nombre == nombre_usuario:
                run = True
                print('Nombre de usuario ya en uso, pruebe uno diferente')

    usuario = Usuario(nombre_usuario, contraseña, email, dinero)
    usuarios.append(usuario)
    return usuarios, usuario.id

def iniciar_sesion(usuarios):
    nombre_usuario = input('Nombre de usuario: ')
    contraseña_usuario = input('Contraseña: ')

    for usuario in usuarios:
        if usuario.nombre == nombre_usuario and usuario.contraseña == contraseña_usuario:
            return usuario.id

def menu(id, usuarios, activos):
    opcion = '0'
    while opcion not in ('1', '2', '3', '4'):
        print(f'Hola {usuarios[id].nombre_usuario}')
        print('Menu de opciones:')
        print('1. Comprar activo')
        print('2. Mostrar Transacciones')
        print('3. Ingresar Dinero')
        print('4. Salir')

        opcion = input('Ingrese una opcion: ')

    if opcion == '1':
        nombre_activo = input('Ingrese activo: ')
        cantidad = int(input('Ingrese cantidad: '))
        for activo in activos:
            if activo.nombre == nombre_activo:
                usuarios[id].compra(activo, cantidad)
        return True

    elif opcion == '2':
        usuarios[id].mostrar_transacciones()
        return True

    elif opcion == '3':
        ingreso = int(input('Cuanto dinero quiere ingresar: '))
        usuarios[id].agregar_dinero(ingreso)
        return True

    elif opcion == '4':
        return False





def inicio(usuarios):
    opcion = '0'
    while opcion != '1' and opcion != '2':
        print('1. Iniciar Sesion\n2. Registrarse')
        opcion = input('Opcion: ')

    if opcion == '1':
        return usuarios, iniciar_sesion(usuarios)
    else:
        return registro(usuarios)

if __name__ == '__main__':

    apple = Accion('Apple', 100, 'APPL')
    activos = []
    activos.append(apple)
    usuarios = []
    usuarios, id = inicio(usuarios)

    run = True
    while run:
        run = menu(id, usuarios, activos)


