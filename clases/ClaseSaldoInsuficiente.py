class ErrorSaldoInsuficiente(Exception):
    def __init__(self, saldo:int, necesario:int) -> None: # Constructor de la clase
        self.saldo = saldo
        self.necesario = necesario

    def diferencia(self)-> int:
        return self.necesario - self.saldo # Devolvemos la diferencia de lo necesario y el saldo

    def __str__(self) -> str: # Creamos la clase str
        return f'Faltan {self.diferencia()}€ para realizar la operacion'