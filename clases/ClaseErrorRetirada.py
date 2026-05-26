class ErrorRetirada(Exception):

    def __init__(self, saldo:int, retirada:int) -> None: # Constructor de la clase
        self.saldo = saldo
        self.retirada = retirada

    def dinero_faltante(self) -> int: # Devolvemos el dinero que falta
        return self.retirada - self.saldo

    def retirada_posible(self) -> int: # Devolvemos un booleano de si es posible hacer esa retirada
        return self.saldo >= self.retirada

    def __str__(self) -> str: # El metodo str de la clase para leerla desde un print
        return (f'Error al retirar dinero\n'
                f'Saldo actual: {self.saldo}$\n'
                f'Retirada: {self.retirada}$\n'
                f'Faltan {self.dinero_faltante()}$')