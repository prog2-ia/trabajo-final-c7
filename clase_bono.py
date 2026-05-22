from clase_activo import Activo

class Bono(Activo): # Clase Bono que hereda de Activo
    def __init__(self, nombre:str, precio:int, codigo:str) -> None:
        super().__init__(nombre, precio)
        self.codigo = codigo

    def __str__(self) -> str:
        return (
            f'Nombre: {self.nombre}\n'
            f'Precio: {self.precio}\n'
            f'Codigo: {self.codigo}\n')

    def tipo(self) -> str:  # Metodo que devuelve el tipo de activo
        return 'Bono'