class Accion():
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return (
            f'Id de la accion: {self.id}\n'
            f'Nombre: {self.nombre}\n'
            f'Precio: {self.precio}\n')

