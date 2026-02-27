from clase_accion import Accion
class Transaccion(Accion):

    cont=0
    def __init__(self, simbolo, precio, usuario, cantidad, fecha):
        super().__init__(simbolo, precio)
        self.usuario = usuario
        self.cantidad = cantidad

        self.fecha = fecha
        type(self).cont+=1

    def calcular_total(self):
        return self.precio * self.cantidad

    def __str__(self):
        return f'{self.usuario}  {self.simbolo} {self.precio} {self.cantidad} {self.fecha}'

    def contador(self):
        return self.cont


