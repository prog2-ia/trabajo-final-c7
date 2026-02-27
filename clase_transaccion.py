from clase_accion import Accion
class Transaccion():

    cont=0
    def __init__(self, usuario, cantidad, tipo, fecha):
        self.usuario = usuario
        self.accion = Accion("+", 6)
        self.cantidad = cantidad
        self.tipo = tipo
        self.fecha = fecha
        type(self).cont+=1

    def calcular_total(self):
        return self.accion.precio * self.cantidad

    def __repr__(self):
        return f'{self.usuario}  {self.accion.simbolo} {self.accion.precio} {self.cantidad} {self.tipo} {self.fecha}'

    def compra(self):
        return self.tipo == "compra"

    def venta(self):
        return self.tipo == "venta"

    def contador(self):
        return self.cont


