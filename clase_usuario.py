from clase_transaccion import Transaccion
from datetime import datetime

class Usuario():
    num_usuarios = 0 # Numero de Usuarios

    def __init__(self, nombre_usuario, contrasena, email, dinero): # Constructor
        self.id = type(self).num_usuarios
        self.__nombre_usuario = nombre_usuario
        self.__contrasena = contrasena
        self.email = email
        self.dinero = dinero
        self.transacciones=[]
        type(self).num_usuarios += 1

    def leer_nombre(self):
        return self.__nombre_usuario
    def leer_contrasena(self):
        return self.__contrasena



    def __str__(self): # Visualizacion simple del objeto
        return f'Id: {self.id}\nNombre usuario: {self.nombre_usuario}\nContrasena: {self.contrasena}\nEmail: {self.email}\nDinero: {self.dinero}'

    def __repr__(self): # Visualizacion completa del objeto
        return (f'Usuario(id={self.id}, '
                f'nombre_usuario={self.nombre_usuario}, '
                f'contrasena={self.contrasena}, '
                f'email={self.email}, '
                f'dinero={self.dinero})')

    def agregar_dinero(self, valor): # Metodo para agregar dinero
        if valor > 0:
            self.dinero += valor
            print(f'Se han anadido correctamente {valor}$, saldo actual: {self.dinero}$')
        else:
            print(f'La cantidad debe ser mayor a 0')

    def sacar_dinero(self, valor): # Metodo para retirar dinero
        if valor < 0:
            print(f'La cantidad debe ser mayor a 0')
        elif valor <= self.dinero:
            self.dinero -= valor
            print(f'Se han retirado correctamente {valor}$, saldo actual: {self.dinero}$')
        else:
            print(f'No tiene {valor}$ en su cuenta')

    @classmethod
    def obtener_num_usuarios(cls): # Metodo de clase para obtener la cantidad de usuarios
        return cls.num_usuarios

    def compra(self,activo,cantidad):
        fecha = datetime.now()
        precio = activo.precio
        p=False
        if self.dinero >= cantidad*precio:
            self.dinero -= cantidad * precio

            for transaccion in self.transacciones:

                if transaccion.activo.nombre==activo.nombre:
                    transaccion.cantidad+=cantidad
                    p=True

            if not p:

                t=Transaccion(activo, self.leer_nombre(), cantidad, fecha)
                self.transacciones.append(t)
        else:
            print(f'No hay saldo suficiente para comprar el/los activos')

    def mostrar_transacciones(self):
        if self.transacciones:
            for i in self.transacciones:
                print(i)
        else:
            print('No hay transacciones')

    def vender(self,transaccion,cantidad):

            fecha = datetime.now()
            precio = transaccion.activo.precio
            self.dinero -= cantidad * precio
            if cantidad == transaccion.cantidad :

                self.transacciones.remove(transaccion)
            else:
                transaccion.cantidad -= cantidad


