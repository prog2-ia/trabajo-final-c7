class ErrorRetirada(Exception):

    def __init__(self, saldo:int, retirada:int) -> None:
        self.saldo = saldo
        self.retirada = retirada

    def dinero_faltante(self) -> int:
        return self.retirada - self.saldo

    def retirada_posible(self) -> int:
        return self.saldo >= self.retirada

    def __str__(self) -> str:
        return (f'Error al retirar dinero\n'
                f'Saldo actual: {self.saldo}$\n'
                f'Retirada: {self.retirada}$\n'
                f'Faltan {self.dinero_faltante()}$')