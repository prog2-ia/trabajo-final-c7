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
                contrasena = datos[1]
                email = datos[2]
                dinero = int(datos[3])
                usuario = Usuario(nombre_usuario, contrasena, email, dinero) # Crear objeto Usuario y anadirlo a la lista
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
            f.write(usuario.leer_nombre() + ' ' + usuario.leer_contrasena() + ' ' + usuario.email + ' ' + str(usuario.dinero) + '\n')


def registro(usuarios): # Funcion para registrar un nuevo usuario
    run = True
    while run:
        run = False
        # Pedir datos al usuario
        nombre_usuario = input('Ingrese su nombre: ')
        contrasena = input('Ingrese su contrasena: ')
        email = input('Ingrese su email: ')
        dinero = int(input('Ingrese su dinero: '))

        for usuario in usuarios: # Comprobar si el nombre ya existe
            if usuario.leer_nombre() == nombre_usuario:
                run = True
                print('Nombre de usuario ya en uso, pruebe uno diferente')

    usuario = Usuario(nombre_usuario, contrasena, email, dinero) # Crear y anadir el nuevo usuario
    usuarios.append(usuario)
    return usuarios, usuario.id, True

def iniciar_sesion(usuarios): # Funcion para iniciar sesion
    buscar = True
    while buscar:
        nombre = input('Nombre de usuario: ')
        contrasena_usuario = input('Contrasena: ')

        for usuario in usuarios: # Buscar coincidencia de usuario y contrasena
            if usuario.leer_nombre() == nombre and usuario.leer_contrasena() == contrasena_usuario:
                return usuario.id
        print('Usuario o contrasena incorrecto')

def menu(id, usuarios, activos): # Menu principal despues de iniciar sesion
    opcion = '0'
    while opcion not in ('1', '2', '3', '4', '5', '6', '7','8','9'): # Validar opcion del menu
        print(f'\nHola {usuarios[id].leer_nombre()}')
        print('Menu de opciones:')
        print('1. Comprar activo')
        print('2. Vender activos')
        print('3. Mostrar Activos')
        print('4. Mostrar Transacciones')
        print('5. Ingresar Dinero')
        print('6. Mostrar Saldo Actual')
        print('7. Mostrar Saldo en activos')
        print('8. Sacar Dinero')
        print('9. Cerrar Sesion')
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
    elif opcion=='2': #Opcion 2: Venta de activos
        opcion=-1
        cantidad=0

        if usuarios[id].transacciones:
            while opcion < 1 or opcion > len(usuarios[id].transacciones)or cantidad < 1 or cantidad > usuarios[id].transacciones[opcion-1].cantidad:
                cont = 0
                for transaccion in usuarios[id].transacciones:
                    cont +=1
                    print(cont,'',transaccion.activo.nombre,' Precio: ',transaccion.activo.precio, ' Cantidad: ',transaccion.cantidad)

                opcion = int(input('Ingrese una opcion: '))
                cantidad = int(input('Ingrese cantidad: '))
                if opcion < 1 or opcion > len(usuarios[id].transacciones) or cantidad < 1 or cantidad > usuarios[id].transacciones[opcion-1].cantidad:
                    print('Opcion no valida...')

                else:
                    usuarios[id].vender(usuarios[id].transacciones[opcion - 1], cantidad)
                    break
        else:
            print('No hay acciones que vender')

        return True

    elif opcion == '3': # Opcion 3: Mostrar activos disponibles
        print('Activos: ')
        for activo in activos:
            print(f'Nombre: {activo.nombre}, Precio: {activo.precio}')
        return True

    elif opcion == '4': # Opcion 4: Mostrar historial de transacciones
        usuarios[id].mostrar_transacciones()
        return True

    elif opcion == '5': # Opcion 5: Ingresar dinero
        print(f'Saldo actual: {usuarios[id].dinero}')
        ingreso = int(input('Cuanto dinero quiere ingresar: '))
        usuarios[id].agregar_dinero(ingreso)
        return True
    elif opcion == '6': # Opcion 6: Mostrar saldo disponible
        print(f'Saldo actual: {usuarios[id].dinero}')
        return True

    elif opcion == '7': # Opcion 7: Calcular valor total en activos
        suma=0
        for transaccion in usuarios[id].transacciones:
            suma+=(transaccion.activo.precio*transaccion.cantidad)
        print(suma)
        return True

    elif opcion == '8': # Opcion 8: Retirar dinero
        print(f'Saldo actual: {usuarios[id].dinero}')
        retirar = int(input('Cuanto dinero quiere retirar: '))
        usuarios[id].sacar_dinero(retirar)
        return True
    elif opcion == '9': # Opcion 9: Cerrar sesión
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

    activos: list = []
    activos = cargar_activos(activos)
    usuarios: list = []
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