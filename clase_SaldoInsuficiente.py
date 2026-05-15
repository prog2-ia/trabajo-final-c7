class ErrorSaldoInsuficiente(Exception):
    def __init__(self, saldo, necesario):
        self.saldo = saldo
        self.necesario = necesario

    def diferencia(self):
        return self.necesario - self.saldo

    def __str__(self):
        return f'Faltan {self.diferencia()}€ para realizar la operacion'