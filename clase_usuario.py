class Usuario():
    num_usuarios = 0 # Numero de Usuarios
    def __init__(self, nombre_usuario, contraseña, email, dinero): # Constructor
        self.id = type(self).num_usuarios
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.email = email
        self.dinero = dinero
        type(self).num_usuarios += 1

    def __str__(self): # Visualizacion simple del objeto
        return f'Id: {self.id}\nNombre usuario: {self.nombre_usuario}\nContraseña: {self.contraseña}\nEmail: {self.email}\nDinero: {self.dinero}'

    def __repr__(self): # Visualizacion completa del objeto
        return (f'Usuario(id={self.id}, '
                f'nombre_usuario={self.nombre_usuario}, '
                f'contraseña={self.contraseña}, '
                f'email={self.email}, '
                f'dinero={self.dinero})')

    def agregar_dinero(self, valor): # Metodo para agregar dinero
        if valor > 0:
            self.dinero += valor
            print(f'Se han añadido correctamente {valor}$, saldo actual: {self.dinero}$')
        else:
            print(f'La cantidad debe ser mayor a 0')

    def sacar_dinero(self, valor): # Metodo para retirar dinero
        if valor < 0:
            print(f'La cantidad debe ser mayor a 0')
        elif valor <= self.dinero:
            self.dinero -= valor
            print(f'Se han retirado correctamente {valor}$, saldo actual: {self.dinero}$')
        else:
            print(f'No tiene {valor}$ en su cuenta')

    @classmethod
    def obtener_num_usuarios(cls): # Metodo de clase para obtener la cantidad de usuarios
        return cls.num_usuarios