from clase_activo import Activo

class Fondo(Activo):
    def __init__(self, nombre, precio, codigo):
        super().__init__(nombre, precio)
        self.codigo = codigo

    def __str__(self):
        return (
            f'Nombre: {self.nombre}\n'
            f'Precio: {self.precio}\n'
            f'Codigo: {self.codigo}\n')

    def tipo(self):
        return 'Fondo'