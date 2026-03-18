from clase_usuario import Usuario
from clase_accion import Accion
from clase_cripto import Cripto
from clase_fondo import Fondo


def leer_usuarios(usuarios): # Funcion para leer los usuarios desde un archivo de texto
    try:
        with open('usuarios.txt', 'r') as f:
            lineas = f.readlines()

        if lineas: # Si hay lineas en el archivo
            for linea in lineas:
                datos = linea.strip().split(' ') # Separar los datos por espacios
                nombre_usuario = datos[0]
                contraseña = datos[1]
                email = datos[2]
                dinero = int(datos[3])
                usuario = Usuario(nombre_usuario, contraseña, email, dinero) # Crear objeto Usuario y añadirlo a la lista
                usuarios.append(usuario)

            return usuarios
        else: # Si el archivo está vacio
            usuarios = []
            return usuarios

    except FileNotFoundError: # Si el archivo no existe, se crea uno vacio
        with open('usuarios.txt', 'w'):
            pass
        usuarios = []
        return usuarios

def guardar_usuarios(usuarios): # Funcion para guardar los usuarios en el archivo
    with open('usuarios.txt', 'w') as f:
        for usuario in usuarios: # Guardamos los datos separados por espacios
            f.write(usuario.nombre_usuario + ' ' + usuario.contraseña + ' ' + usuario.email + ' ' + str(usuario.dinero) + '\n')


def registro(usuarios): # Funcion para registrar un nuevo usuario
    run = True
    while run:
        run = False
        # Pedir datos al usuario
        nombre_usuario = input('Ingrese su nombre: ')
        contraseña = input('Ingrese su contraseña: ')
        email = input('Ingrese su email: ')
        dinero = int(input('Ingrese su dinero: '))

        for usuario in usuarios: # Comprobar si el nombre ya existe
            if usuario.nombre_usuario == nombre_usuario:
                run = True
                print('Nombre de usuario ya en uso, pruebe uno diferente')

    usuario = Usuario(nombre_usuario, contraseña, email, dinero) # Crear y añadir el nuevo usuario
    usuarios.append(usuario)
    return usuarios, usuario.id, True

def iniciar_sesion(usuarios): # Funcion para iniciar sesion
    buscar = True
    while buscar:
        nombre = input('Nombre de usuario: ')
        contraseña_usuario = input('Contraseña: ')

        for usuario in usuarios: # Buscar coincidencia de usuario y contraseña
            if usuario.nombre_usuario == nombre and usuario.contraseña == contraseña_usuario:
                return usuario.id
        print('Usuario o contraseña incorrecto')

def menu(id, usuarios, activos): # Menu principal despues de iniciar sesion
    opcion = '0'
    while opcion not in ('1', '2', '3', '4', '5', '6', '7','8'): # Validar opcion del menu
        print(f'\nHola {usuarios[id].nombre_usuario}')
        print('Menu de opciones:')
        print('1. Comprar activo')
        print('2. Mostrar Activos')
        print('3. Mostrar Transacciones')
        print('4. Ingresar Dinero')
        print('5. Mostrar Saldo Actual')
        print('6. Mostrar Saldo en activos')
        print('7. Sacar Dinero')
        print('8. Cerrar Sesion')
        opcion = input('Ingrese una opcion: ')
        print()
    if opcion == '1': #Opcion 1: Comprar activo
        opcion = -1
        while opcion < 1 or opcion > len(activos) : # Validar eleccion de activo
            for i in range(len(activos)):
                print(f'{i+1}. {activos[i].nombre}: {activos[i].precio}$')

            opcion = int(input('Ingrese una opcion: '))
            if opcion < 1 or opcion > len(activos) :
                print('Opcion no valida...')
        cantidad = int(input('Ingrese cantidad: '))
        usuarios[id].compra(activos[opcion-1], cantidad)
        return True

    elif opcion == '2': # Opcion 2: Mostrar activos disponibles
        print('Activos: ')
        for activo in activos:
            print(f'Nombre: {activo.nombre}, Precio: {activo.precio}')
        return True

    elif opcion == '3': # Opcion 3: Mostrar historial de transacciones
        usuarios[id].mostrar_transacciones()
        return True

    elif opcion == '4': # Opcion 4: Ingresar dinero
        print(f'Saldo actual: {usuarios[id].dinero}')
        ingreso = int(input('Cuanto dinero quiere ingresar: '))
        usuarios[id].agregar_dinero(ingreso)
        return True
    elif opcion == '5': # Opcion 5: Mostrar saldo disponible
        print(f'Saldo actual: {usuarios[id].dinero}')
        return True

    elif opcion == '6': # Opcion 6: Calcular valor total en activos
        suma=0
        for transaccion in usuarios[id].transacciones:
            suma+=(transaccion.activo.precio*transaccion.cantidad)
        print(suma)
        return True

    elif opcion == '7': # Opcion 7: Retirar dinero
        print(f'Saldo actual: {usuarios[id].dinero}')
        retirar = int(input('Cuanto dinero quiere retirar: '))
        usuarios[id].sacar_dinero(retirar)
        return True
    elif opcion == '8': # Opcion 8: Cerrar sesión
        print('Cerrando Sesion...')
        print()
        guardar_usuarios(usuarios) # Guardar usuarios antes de salir
        return False


def cargar_activos(activos): # Funcion para cargar activos desde archivo
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


def inicio(usuarios): # Menú inicial del programa
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

if __name__ == '__main__': # Inicio del programa

    activos = []
    activos = cargar_activos(activos)
    usuarios = []
    usuarios = leer_usuarios(usuarios)

    run = True
    while run: # Bucle principal del programa
        usuarios, id, run = inicio(usuarios)
        if run == True:
            sesion = True
        else:
            sesion = False
        while sesion:
            sesion = menu(id, usuarios, activos)
