from  clases.ClaseUsuario import Usuario
import pickle
import os

class GestorBackup:

    @staticmethod
    def crear_backup(usuarios:list[Usuario], nombre_archivo: str ='backups/backup_sistema.pickle') -> None:
        # Creamos un metodo estatico de la clase
        if not os.path.exists('../backups'):
            os.mkdir('../backups')

        try:
            with open(nombre_archivo, 'wb') as f: # Intentamos abrir el archivo o damos el error
                pickle.dump(usuarios, f)

            print(f'Respaldo creado en {nombre_archivo}')

        except Exception as e: # En caso de error de volver un print del error
            print(f'Error al crear respaldo: {e}')

    @staticmethod
    def restaurar_sistema(nombre_archivo: str ='backups/backup_sistema.pickle') -> list[Usuario] | None: # Creamos otro metodo estatico

        if os.path.exists(nombre_archivo):

            try:
                with open(nombre_archivo, 'rb') as f: # En caso ce existir el archivo  devolvemos una lista de los usuarios
                    return list[Usuario](pickle.load(f))

            except EOFError:
                return [] # Devolvemos una lista vacia

        return None