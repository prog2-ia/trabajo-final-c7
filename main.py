from clase_usuario import Usuario
from clase_accion import Accion
from clase_cripto import Cripto
from clase_fondo import Fondo


def leer_usuarios(usuarios):
    try:
        with open('usuarios.txt', 'r') as f:
            lineas = f.readlines()

        if lineas:
            for linea in lineas:
                datos = linea.strip().split(' ')
                nombre_usuario = datos[0]
                contraseña = datos[1]
                email = datos[2]
                dinero = int(datos[3])
                usuario = Usuario(nombre_usuario, contraseña, email, dinero)
                usuarios.append(usuario)

            return usuarios
        else:
            usuarios = []
            return usuarios

    except FileNotFoundError:
        with open('usuarios.txt', 'w'):
            pass
        usuarios = []
        return usuarios

def guardar_usuarios(usuarios):
    with open('usuarios.txt', 'w') as f:
        for usuario in usuarios:
            f.write(usuario.nombre_usuario + ' ' + usuario.contraseña + ' ' + usuario.email + ' ' + str(usuario.dinero) + '\n')


def registro(usuarios):
    run = True
    while run:
        run = False
        nombre_usuario = input('Ingrese su nombre: ')
        contraseña = input('Ingrese su contraseña: ')
        email = input('Ingrese su email: ')
        dinero = int(input('Ingrese su dinero: '))

        for usuario in usuarios:
            if usuario.nombre_usuario == nombre_usuario:
                run = True
                print('Nombre de usuario ya en uso, pruebe uno diferente')

    usuario = Usuario(nombre_usuario, contraseña, email, dinero)
    usuarios.append(usuario)
    return usuarios, usuario.id, True

def iniciar_sesion(usuarios):
    buscar = True
    while buscar:
        nombre = input('Nombre de usuario: ')
        contraseña_usuario = input('Contraseña: ')

        for usuario in usuarios:
            if usuario.nombre_usuario == nombre and usuario.contraseña == contraseña_usuario:
                return usuario.id
        print('Usuario o contraseña incorrecto')

def menu(id, usuarios, activos):
    opcion = '0'
    while opcion not in ('1', '2', '3', '4', '5', '6', '7'):
        print(f'\nHola {usuarios[id].nombre_usuario}')
        print('Menu de opciones:')
        print('1. Comprar activo')
        print('2. Mostrar Activos')
        print('3. Mostrar Transacciones')
        print('4. Ingresar Dinero')
        print('5. Mostrar Saldo Actual')
        print('6. Sacar Dinero')
        print('7. Cerrar Sesion')

        opcion = input('Ingrese una opcion: ')

    if opcion == '1':
        opcion = -1
        while opcion < 1 or opcion > len(activos) :
            for i in range(len(activos)):
                print(f'{i+1}. {activos[i].nombre}: {activos[i].precio}$')

            opcion = int(input('Ingrese una opcion: '))
            if opcion < 1 or opcion > len(activos) :
                print('Opcion no valida...')
        cantidad = int(input('Ingrese cantidad: '))
        usuarios[id].compra(activos[opcion-1], cantidad)
        return True

    elif opcion == '2':
        print('Activos: ')
        for activo in activos:
            print(f'Nombre: {activo.nombre}, Precio: {activo.precio}')
        return True

    elif opcion == '3':
        usuarios[id].mostrar_transacciones()
        return True

    elif opcion == '4':
        print(f'Saldo actual: {usuarios[id].dinero}')
        ingreso = int(input('Cuanto dinero quiere ingresar: '))
        usuarios[id].agregar_dinero(ingreso)
        return True
    elif opcion == '5':
        print(f'Saldo actual: {usuarios[id].dinero}')
        return True

    elif opcion == '6':
        print(f'Saldo actual: {usuarios[id].dinero}')
        retirar = int(input('Cuanto dinero quiere retirar: '))
        usuarios[id].sacar_dinero(retirar)
        return True
    elif opcion == '7':
        print('Cerrando Sesion...')
        guardar_usuarios(usuarios)
        return False


def cargar_activos(activos):
    try:
        with open('activos.txt', 'r') as f:
            lineas = f.readlines()

        if lineas:
            for linea in lineas:
                datos = linea.strip().split(' ')
                nombre = datos[0]
                precio = int(datos[1])
                codigo = datos[2]
                tipo =  datos[3].strip()
                if tipo == 'Accion':
                    activo = Accion(nombre, precio, codigo)
                elif tipo == 'Fondo':
                    activo = Fondo(nombre, precio, codigo)
                else:
                    activo = Cripto(nombre, precio, codigo)
                activos.append(activo)

            return activos
        else:
            activos = []
            return activos

    except FileNotFoundError:
        with open('activos.txt', 'w'):
            pass
        activos = []
        return activos


def inicio(usuarios):
    opcion = '0'
    while opcion not in ('1', '2', '3'):
        print('1. Iniciar Sesion')
        print('2. Registrarse')
        print('3. Salir')
        opcion = input('Opcion: ')

        if opcion == '1':
            if usuarios:
                return usuarios, iniciar_sesion(usuarios), True
            else:
                print('No hay usuarios registrados')
                opcion = '0'

        elif opcion == '2':
            return registro(usuarios)
        elif opcion == '3':
            return usuarios, None, False

if __name__ == '__main__':

    activos = []
    activos = cargar_activos(activos)
    usuarios = []
    usuarios = leer_usuarios(usuarios)

    run = True
    while run:
        usuarios, id, run = inicio(usuarios)
        if run == True:
            sesion = True
        else:
            sesion = False
        while sesion:
            sesion = menu(id, usuarios, activos)