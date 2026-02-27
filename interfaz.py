from clase_transaccion import Transaccion
from clase_usuario import Usuario

class Interfaz:
    def __init__(self,usuario,simulador,estado_actual,transacciones):
        self.estado_actual = estado_actual
        self.transacciones = transacciones
        self.usuario = usuario
        self.estado_actual = estado_actual
        self.simulador = simulador

    def mostrar_menu(self):
        pass
