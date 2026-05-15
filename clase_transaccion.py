from clase_activo import Activo
class Transaccion():

    cont=0 #contador total de transacciones creadas
    def __init__(self, activo, usuario, cantidad, fecha):
        self.activo = activo
        self.usuario = usuario
        self.cantidad = cantidad
        self.fecha = fecha
        type(self).cont+=1

    def calcular_total(self):  # Devuelve el valor total de la transaccion
        return self.precio * self.cantidad

    def tipo(self): # Devuelve el tipo de activo
        return self.activo.tipo()

    def __str__(self): #texto de la transaccion
        return (f'Usuario: {self.usuario}\n'
                f'Nombre: {self.activo.nombre}\n'
                f'Cantidad: {self.cantidad}\n'
                f'Tipo de activo: {self.tipo()}\n'
                f'Fecha: {self.fecha}\n')

    def contador(self): # Devuelve el numero total de transacciones creadas
        return self.cont


