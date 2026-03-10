from clase_activo import Activo
class Transaccion():

    cont=0
    def __init__(self, activo, usuario, cantidad, fecha):
        self.activo = activo
        self.usuario = usuario
        self.cantidad = cantidad
        self.fecha = fecha
        type(self).cont+=1

    def calcular_total(self):
        return self.precio * self.cantidad

    def tipo(self):
        return self.activo.tipo()

    def __str__(self):
        return (f'Usuario: {self.usuario}\n'
                f'Nombre: {self.activo.nombre}\n'
                f'Cantidad: {self.cantidad}\n'
                f'Tipo de activo: {self.tipo()}\n'
                f'Fecha: {self.fecha}\n')

    def contador(self):
        return self.cont


