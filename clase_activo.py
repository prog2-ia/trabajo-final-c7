from abc import ABC, abstractmethod

class Activo(ABC): # Clase base de activos
    def __init__(self, nombre:str, precio:int) -> None:
        self.nombre = nombre
        self.precio = precio

    def __str__(self) -> str:
        return (
            f'Nombre: {self.nombre}\n'
            f'Precio: {self.precio}\n')

    @abstractmethod
    def tipo(self) -> str:
        pass