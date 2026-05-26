from  clases.ClaseAccion import Accion
from  clases.ClaseFondo import Fondo
from  clases.ClaseCripto import Cripto
from  clases.ClaseBono import Bono
class Transaccion():

    cont=0 #contador total de transacciones creadas
    def __init__(self, activo: Accion | Fondo | Cripto | Bono, usuario: str, cantidad: int, fecha: str) -> None:
        self.activo = activo
        self.usuario = usuario
        self.cantidad = cantidad
        self.fecha = fecha
        type(self).cont+=1 # Sumamos uno para ver la cantidad de objetos creados en la clase

    def tipo(self)->str: # Devuelve el tipo de activo
        return self.activo.tipo()

    def __str__(self)->str: #texto de la transaccion
        return (f'Usuario: {self.usuario}\n'
                f'Nombre: {self.activo.nombre}\n'
                f'Cantidad: {self.cantidad}\n'
                f'Tipo de activo: {self.tipo()}\n'
                f'Fecha: {self.fecha}\n')

    def contador(self)->int: # Devuelve el número total de transacciones creadas
        return self.cont


