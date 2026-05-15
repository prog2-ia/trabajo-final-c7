class ErrorRetirada(Exception):

    def __init__(self, saldo, retirada):
        self.saldo = saldo
        self.retirada = retirada

    def dinero_faltante(self):
        return self.retirada - self.saldo

    def retirada_posible(self):
        return self.saldo >= self.retirada

    def __str__(self):
        return (f'Error al retirar dinero\n'
                f'Saldo actual: {self.saldo}$\n'
                f'Retirada: {self.retirada}$\n'
                f'Faltan {self.dinero_faltante()}$')