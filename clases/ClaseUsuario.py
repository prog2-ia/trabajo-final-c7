from  clases.ClaseTransaccion import Transaccion
from datetime import datetime
from  clases.ClaseSaldoInsuficiente import ErrorSaldoInsuficiente
from  clases.ClaseErrorRetirada import ErrorRetirada
from  clases.ClaseAccion import Accion
from  clases.ClaseFondo import Fondo
from  clases.ClaseCripto import Cripto
from  clases.ClaseBono import Bono

class Usuario():
    num_usuarios = 0 # Numero de Usuarios

    def __init__(self, nombre_usuario: str, contrasena: str, email: str, dinero: int) -> None: #constructor
        self.id = type(self).num_usuarios
        self.__nombre_usuario = nombre_usuario
        self.__contrasena = contrasena
        self.email = email
        self.dinero = dinero
        self.transacciones: list[Transaccion] = [] # Devolvemos una lista de transacciones vacia
        type(self).num_usuarios += 1

    def leer_nombre(self) -> str: # Devolvemos el nombre privado del objeto
        return self.__nombre_usuario
    def leer_contrasena(self) -> str: # Devolvemos la contraseña privada del objeto
        return self.__contrasena

    def __str__(self) -> str: # Creamos un str del objeto
        return (f'Id: {self.id}\n'
                f'Nombre usuario: {self.__nombre_usuario}\n'
                f'Contrasena: {self.__contrasena}\n'
                f'Email: {self.email}\n'
                f'Dinero: {self.dinero}')

    def __repr__(self) -> str: # Creamos la representacion mas especifica del objeto
        return (f'Usuario(id={self.id}, '
                f'nombre_usuario={self.__nombre_usuario}, '
                f'contrasena={self.__contrasena}, '
                f'email={self.email}, '
                f'dinero={self.dinero})')

    def agregar_dinero(self, valor: int) -> None:# Metodo para agregar dinero
        if valor > 0:
            self.dinero += valor
            print(f'Se han anadido correctamente {valor}$, saldo actual: {self.dinero}$')
        else:
            print(f'La cantidad debe ser mayor a 0')

    def sacar_dinero(self, valor: int) -> None: # Metodo para retirar dinero
        if valor < 0:
            print(f'La cantidad debe ser mayor a 0')
        elif valor <= self.dinero:
            self.dinero -= valor
            print(f'Se han retirado correctamente {valor}$, saldo actual: {self.dinero}$') # Devolvemos cuanto dinero se ha retirado
        else:
            raise ErrorRetirada(self.dinero, valor)

    @classmethod
    def obtener_num_usuarios(cls) -> int: # Metodo de clase para obtener la cantidad de usuarios
        return cls.num_usuarios

    def compra(self, activo: Accion | Fondo | Cripto | Bono, cantidad: int) -> None: # Creamos la compra
        fecha = str(datetime.now()) # Guardamos la fecha del momento
        precio = activo.precio
        p=False
        if self.dinero >= cantidad*precio:
            self.dinero -= cantidad * precio

            for transaccion in self.transacciones: # Miramos las transacciones para el caso de ya haber una del activo

                if transaccion.activo.nombre==activo.nombre:
                    transaccion.cantidad+=cantidad
                    p=True

            if not p:

                t=Transaccion(activo, self.leer_nombre(), cantidad, fecha)
                self.transacciones.append(t) # Creamos la transaccion y la guardamos
        else:
            raise ErrorSaldoInsuficiente(self.dinero,cantidad*precio) # Devolvemos el error

    def mostrar_transacciones(self) -> None:
        if self.transacciones:
            for i in self.transacciones: # Mostramos las transacciones o por defecto si no hay
                print(i)
        else:
            print('No hay transacciones')

    def vender(self, transaccion: Transaccion, cantidad: int, activos: list[Accion | Fondo | Cripto | Bono]) -> None: # Metodo para vender las acciones
        assert cantidad <= transaccion.cantidad, 'No puedes vender mas activos de los que tienes'
        precio_actual = 0

        for activo in activos:
            if activo.nombre == transaccion.activo.nombre: # Miramos si axiste una transaccion del activo introducido
                precio_actual = activo.precio
                break

        self.dinero += cantidad * precio_actual

        if cantidad == transaccion.cantidad:
            self.transacciones.remove(transaccion) # Añadimos el dinero y quitamos la transaccion
        else:
            transaccion.cantidad -= cantidad # Quitamos una cantidad en caso de no venderla entera
