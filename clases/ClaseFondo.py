from  clases.ClaseActivo import Activo

class Fondo(Activo): # Clase Fondo que hereda de Activo
    def __init__(self, nombre:str, precio:int, codigo:str) -> None:
        super().__init__(nombre, precio)
        self.codigo = codigo

    def __str__(self) -> str:
        return (
            f'Nombre: {self.nombre}\n'
            f'Precio: {self.precio}\n'
            f'Codigo: {self.codigo}\n')

    def tipo(self) -> str: # Metodo que indica tipo de activo
        return 'Fondo'