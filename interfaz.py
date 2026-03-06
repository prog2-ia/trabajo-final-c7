from clase_transaccion import Transaccion
from clase_usuario import Usuario

class Interfaz:

    def mostrar_menu(self):

            print("----- simulador de inversion -----")
            print("1 ver usuario")
            print("2 comprar accion")
            print("3 vender accion")
            print("4 ver cartera")
            print("5 ver transacciones")
            print("0 salir")

            opcion = input("elige opcion: ")

            if opcion == "1":
                self.ver_usuario()
            elif opcion == "2":
                pass
                #self.comprar()
            elif opcion == "3":
                pass
                #self.vender()
            elif opcion == "4":
                self.ver_cartera()
            elif opcion == "5":
                self.ver_transacciones()
            elif opcion == "0":
                self.salir()
            else:
                print("opcion no valida")

    def salir(self):
        return False

    def ver_usuario(self):
        pass


    def ver_cartera(self):
        pass


    def ver_transacciones(self):
        pass


