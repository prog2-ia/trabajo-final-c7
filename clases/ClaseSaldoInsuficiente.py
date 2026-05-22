class ErrorSaldoInsuficiente(Exception):
    def __init__(self, saldo:int, necesario:int) -> None:
        self.saldo = saldo
        self.necesario = necesario

    def diferencia(self)-> int:
        return self.necesario - self.saldo

    def __str__(self) -> str:
        return f'Faltan {self.diferencia()}€ para realizar la operacion'