from clase_activo import Activo

class Cripto(Activo): # Clase Cripto que hereda de Activo
    def __init__(self, nombre, precio, codigo):
        super().__init__(nombre, precio)
        self.codigo = codigo

    def __str__(self):
        return (
            f'Nombre: {self.nombre}\n'
            f'Precio: {self.precio}\n'
            f'Codigo: {self.codigo}\n')

    def tipo(self): # Metodo que indica el tipo de activo
        return 'Cripto'