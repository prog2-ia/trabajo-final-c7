import pickle
import os

class GestorBackup:

    @staticmethod
    def crear_backup(usuarios, nombre_archivo='backups/backup_sistema.pickle'):

        if not os.path.exists('backups'):
            os.mkdir('backups')

        try:
            with open(nombre_archivo, 'wb') as f:
                pickle.dump(usuarios, f)

            print(f'Respaldo creado en {nombre_archivo}')

        except Exception as e:
            print(f'Error al crear respaldo: {e}')

    @staticmethod
    def restaurar_sistema(nombre_archivo='backups/backup_sistema.pickle'):

        if os.path.exists(nombre_archivo):

            try:
                with open(nombre_archivo, 'rb') as f:
                    return pickle.load(f)

            except EOFError:
                return []

        return None