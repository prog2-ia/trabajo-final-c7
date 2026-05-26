from clases.ClaseUsuario import Usuario
from clases.ClaseAccion import Accion
from clases.ClaseCripto import Cripto
from clases.ClaseBono import Bono
from clases.ClaseFondo import Fondo
from clases.ClaseSaldoInsuficiente import ErrorSaldoInsuficiente
from clases.ClaseErrorRetirada import ErrorRetirada
from clases.ClaseTransaccion import Transaccion
from clases.ClaseGestorBackup import GestorBackup
import random
import os
import sys

if getattr(sys, 'frozen', False):# si no se pone esto no va el ejecutable junto a las carpetas
    BASE_DIR = sys._MEIPASS
    SAVE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SAVE_DIR = BASE_DIR

RUTA_DATOS = os.path.join(BASE_DIR, 'datos')
RUTA_GUARDADO = os.path.join(SAVE_DIR, 'datos')

os.makedirs(RUTA_GUARDADO, exist_ok=True)

def leer_usuarios(usuarios: list[Usuario]) -> list[Usuario]: # Funcion para leer los usuarios desde un archivo de texto
    try:
        ruta_usuarios = os.path.join(RUTA_GUARDADO, 'usuarios.txt')

        if not os.path.exists(ruta_usuarios):
            open(ruta_usuarios, 'a').close()

        with open(ruta_usuarios, 'r', encoding='utf-8') as f:
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
        with open(os.path.join(RUTA_GUARDADO, 'usuarios.txt'), 'w', encoding='utf-8'):
            pass
        usuarios = []
        return usuarios
def guardar_activos_usuario(usuarios: list[Usuario], id: int) -> None:
    nombre_fichero = os.path.join(
        RUTA_GUARDADO,
        f'usuario_activo_{usuarios[id].leer_nombre()}.txt'
    ) # Creamos el nombre del archivo
    with open(nombre_fichero, 'w',encoding='utf-8') as f:
        for transaccion in usuarios[id].transacciones: # Escribimos los datos en el fichero
            f.write(str(transaccion))

def leer_activos_usuario(usuarios: list[Usuario],id: int,activos: list[Accion | Fondo | Bono | Cripto]) -> None:
    i = 0
    try:

        nombre_fichero = os.path.join(
            RUTA_GUARDADO,
            f'usuario_activo_{usuarios[id].leer_nombre()}.txt'
        ) # Creamos el nombre
        with open(nombre_fichero, 'r',encoding='utf-8') as f:
            lineas = f.readlines()
            while i < len(lineas): # Guardamos cada linea segun la informacion
                nombre = lineas[i].split()[1]
                nombre_activo = lineas[i+1].split()[1]
                cantidad = int(lineas[i+2].split()[1])
                fecha = lineas[i+4][7:].strip()
                j = 0
                for activo in activos:
                    if activo.nombre == nombre_activo:
                        break
                    j += 1
                t = Transaccion(activos[j], nombre, cantidad, fecha) # Creamos la transaccion
                usuarios[id].transacciones.append(t) # La añadimos al usuario
                i+=5


    except FileNotFoundError:
        print('Error')


def guardar_usuarios(usuarios: list[Usuario]) -> None: # Funcion para guardar los usuarios en el archivo
    with open(os.path.join(RUTA_GUARDADO, 'usuarios.txt'), 'w', encoding='utf-8') as f:
        for usuario in usuarios: # Guardamos los datos separados por espacios
            f.write(usuario.leer_nombre() + ' ' + usuario.leer_contrasena() + ' ' + usuario.email + ' ' + str(usuario.dinero) + '\n')


def registro(usuarios: list[Usuario]) -> tuple[list[Usuario], int, bool]: # Funcion para registrar un nuevo usuario
    run = True
    while run:
        run = False
        # Pedir datos al usuario
        nombre_usuario = input('Ingrese su nombre: ')
        contrasena = input('Ingrese su contrasena: ')
        email = input('Ingrese su email: ')
        while True:
            try:
                dinero = int(input('Ingrese su dinero: ')) # Verificamos que haya ingresado un numero valido
                break
            except ValueError:
                print('Debe ingresar un numero')

        for usuario in usuarios: # Comprobar si el nombre ya existe
            if usuario.leer_nombre() == nombre_usuario:
                run = True
                print('Nombre de usuario ya en uso, pruebe uno diferente')

    usuario = Usuario(nombre_usuario, contrasena, email, dinero) # Crear y anadir el nuevo usuario
    usuarios.append(usuario)
    return usuarios, usuario.id, True

def iniciar_sesion(usuarios: list[Usuario]) -> int: # Funcion para iniciar sesion
    buscar = True
    while buscar:
        nombre = input('Nombre de usuario: ')
        contrasena_usuario = input('Contrasena: ')

        for usuario in usuarios: # Buscar coincidencia de usuario y contrasena
            if usuario.leer_nombre() == nombre and usuario.leer_contrasena() == contrasena_usuario:
                return usuario.id
        print('Usuario o contrasena incorrecto')
    return -1

def menu(id: int,usuarios: list[Usuario],activos: list[Accion | Fondo | Bono | Cripto]) -> tuple[bool, list[Accion | Fondo | Bono | Cripto]]: # Menu principal despues de iniciar sesion
    opcion: int | str = '0'
    while opcion not in ('1', '2', '3', '4', '5', '6', '7','8','9'): # Validar opcion del menu
        activos = activoRandom(activos)
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

            try:
                opcion = int(input('Ingrese una opcion: ')) # Guardamos la opcion con sus excepciones
            except ValueError:
                print('Debe ingresar un numero') # Miramos las expcepciones para ver los numeros validos
                opcion = -1
            if opcion < 1 or opcion > len(activos) :
                print('Opcion no valida...')
        cantidad = 0
        while cantidad < 1:
            try:
                cantidad = int(input('Ingrese cantidad: ')) # Guardamos la cantidad y sus excepciones
            except ValueError:
                print('Debe ingresar un numero')
                cantidad = 0
            if cantidad < 1:
                print('Opcion no valida...')
        try:
            usuarios[id].compra(activos[opcion - 1], cantidad) # Intentamos la compra

        except ErrorSaldoInsuficiente as e:
            print(e)
        return True,activos
    elif opcion=='2': #Opcion 2: Venta de activos
        opcion=-1
        cantidad=0
        if usuarios[id].transacciones: # Mientras la opción o la cantidad no sean válidas, seguimos pidiendo datos
            while opcion < 1 or opcion > len(usuarios[id].transacciones)or cantidad < 1 or cantidad > usuarios[id].transacciones[opcion-1].cantidad:
                cont = 0
                for transaccion in usuarios[id].transacciones:
                    cont += 1

                    precio_actual = transaccion.activo.precio # Guardamos el precio del activo del momento

                    for activo in activos:
                        if activo.nombre == transaccion.activo.nombre:
                            precio_actual = activo.precio
                            break
                    # Mostramos la info de cada transacción
                    print(cont, '', transaccion.activo.nombre,' Precio: ', precio_actual,' Cantidad: ', transaccion.cantidad)

                try: # Pedimos al usuario qué transacción quiere vender y cuánta cantidad
                    opcion = int(input('Ingrese una opcion: '))
                    cantidad = int(input('Ingrese cantidad: '))
                except ValueError:
                    print('Debe ingresar un numero')
                    opcion = -1
                    cantidad = 0
                 # Validamos que la opción y la cantidad sean correctas
                if opcion < 1 or opcion > len(usuarios[id].transacciones) or cantidad < 1 or cantidad > usuarios[id].transacciones[opcion-1].cantidad:
                    print('Opcion no valida...')

                else:
                    usuarios[id].vender(usuarios[id].transacciones[opcion - 1],cantidad,activos)
                    break
        else:
            print('No hay acciones que vender')

        return True,activos

    elif opcion == '3': # Opcion 3: Mostrar activos disponibles
        print('Activos: ')
        activos = activoRandom(activos)
        for activo in activos:
            print(f'Nombre: {activo.nombre}, Precio: {activo.precio}')
        return True,activos

    elif opcion == '4': # Opcion 4: Mostrar historial de transacciones
        usuarios[id].mostrar_transacciones()
        return True,activos

    elif opcion == '5': # Opcion 5: Ingresar dinero
        print(f'Saldo actual: {usuarios[id].dinero}')
        try:
            ingreso = int(input('Cuanto dinero quiere ingresar: ')) # Comprobamos que el numero sea correcto
        except ValueError:
            print('Debe ingresar un numero')
            ingreso = 0
        usuarios[id].agregar_dinero(ingreso)
        return True,activos
    elif opcion == '6': # Opcion 6: Mostrar saldo disponible
        print(f'Saldo actual: {usuarios[id].dinero}')
        return True,activos

    elif opcion == '7': # Opcion 7: Calcular valor total en activos
        suma=0
        for transaccion in usuarios[id].transacciones:
            suma+=(transaccion.activo.precio*transaccion.cantidad) # Guardamos la suma total de los valores de las transacciones
        print(suma)
        return True,activos

    elif opcion == '8': # Opcion 8: Retirar dinero
        print(f'Saldo actual: {usuarios[id].dinero}')
        try:
            retirar = int(input('Cuanto dinero quiere retirar: ')) # Comprobamos que el valor sea valido
        except ValueError:
            print('Debe ingresar un numero')
            retirar = 0
        try:
            usuarios[id].sacar_dinero(retirar) # Intentamos retirar el dinero en caso de ser posible

        except ErrorRetirada as e:
            print(e)
        return True,activos
    elif opcion == '9': # Opcion 9: Cerrar sesión
        print('Cerrando Sesion...')
        print()
        guardar_usuarios(usuarios) # Guardar usuarios antes de salir
        guardar_activos_usuario(usuarios, id)
        GestorBackup.crear_backup(usuarios)
        return False,activos
    return False, activos

def cargar_activos() -> list[Accion | Fondo | Bono | Cripto]:
    activos: list[Accion | Fondo | Bono | Cripto] = [] # Borramos la lista de activos  en caso de no estar vacia
    try:
        with open(os.path.join(RUTA_DATOS, 'activos.txt'), 'r', encoding='utf-8') as f:
            lineas = f.readlines() # Leemos el fichero de activos

        if lineas:
            for linea in lineas:
                datos = linea.strip().split(' ')
                nombre = datos[0]
                precio = int(datos[1])
                codigo = datos[2]
                tipo =  datos[3].strip() # Guardamos los datos segun los espacios en el fichero
                activo: Accion | Fondo | Bono | Cripto
                if tipo == 'Accion':
                    activo = Accion(nombre, precio, codigo)
                elif tipo == 'Fondo':
                    activo = Fondo(nombre, precio, codigo)
                elif tipo == 'Bono':
                    activo = Bono(nombre, precio, codigo)
                else:
                    activo = Cripto(nombre, precio, codigo)
                activos.append(activo) # Creamos el activo segun su tipo

            return activos # Devolvemos los activos
        else:
            activos = []
            return activos # Devolvemos la lista de activos vacia

    except FileNotFoundError:
        with open(os.path.join(RUTA_DATOS, 'activos.txt'), 'w', encoding='utf-8'): # Creamos el archivo en caso de no existir
            pass
        activos = []
        return activos


def inicio(usuarios: list[Usuario]) -> tuple[list[Usuario], int | None, bool]: # Menú inicial del programa
    opcion = '0'
    while opcion not in ('1', '2', '3'):
        print('1. Iniciar Sesion')
        print('2. Registrarse')
        print('3. Salir')
        opcion = input('Opcion: ') # Guardamos la opcion

        if opcion == '1':
            if usuarios:
                return usuarios, iniciar_sesion(usuarios), True # Iniciamos sesion
            else:
                print('No hay usuarios registrados')
                opcion = '0'

        elif opcion == '2':
            return registro(usuarios) # Registramos
        elif opcion == '3':
            return usuarios, None, False # Nos salimos
    return usuarios, None, False

def activoRandom(activos: list[Accion | Fondo | Bono | Cripto]) -> list[Accion | Fondo | Bono | Cripto]:
    with open(os.path.join(RUTA_DATOS, 'activos.txt'), 'r', encoding='utf-8') as f:
        lineas = f.readlines()

    nuevas_lineas = []


    for linea in lineas:
        datos = linea.strip().split(' ')
        precio = int(datos[1])
        rand = random.randint(90, 110)
        nuev = int(precio * (rand / 100)) # Creamos un sistema que modifica el precio entre un 10 por ciento
        if nuev<10:
            nuevas_lineas.append(f'{datos[0]} {precio} {datos[2]} {datos[3]}\n')
        else:
            nuevas_lineas.append(f'{datos[0]} {nuev} {datos[2]} {datos[3]}\n')

    with open(os.path.join(RUTA_DATOS, 'activos.txt'), 'w', encoding='utf-8') as f:
        f.writelines(nuevas_lineas) # Guardamos los datos en el fichero
    return cargar_activos() # Cargamos los activos del fichero


# Inicio del programa
if __name__ == '__main__':

    activos: list[Accion | Fondo | Bono | Cripto] = cargar_activos()

    usuarios: list[Usuario] = []
    usuarios = leer_usuarios(usuarios)

    # Guardamos la lista de activos y de usuarios

    if not usuarios:
        backup = GestorBackup.restaurar_sistema() # Llamamos al restaurar sistema del gestorBackup

        if backup is not None:
            usuarios = backup

    run = True

    while run:
        usuarios, id, run = inicio(usuarios) # Iniciamos sesion

        if run and id is not None:
            sesion = True
            leer_activos_usuario(usuarios, id, activos) # Leemos los activos

            while sesion:
                sesion, activos = menu(id, usuarios, activos) # Iniciamos el menu con el usuario el id y los activos del momento

        else:
            sesion = False # Cerramos la sesion