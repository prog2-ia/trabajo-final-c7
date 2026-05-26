from clases.ClaseUsuario import Usuario
import pickle
import os
import sys

if getattr(sys, 'frozen', False): # si no se pone esto no va el ejecutable junto a las carpetas
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RUTA_BACKUPS = os.path.join(BASE_DIR, 'backups')
os.makedirs(RUTA_BACKUPS, exist_ok=True)


class GestorBackup:

    @staticmethod
    def crear_backup(usuarios: list[Usuario], nombre_archivo: str = 'backups/backup_sistema.pickle') -> None:
        try:
            ruta_backup = os.path.join(RUTA_BACKUPS, 'backup_sistema.pickle')

            with open(ruta_backup, 'wb') as f:
                pickle.dump(usuarios, f)

            print(f'Respaldo creado en {ruta_backup}')

        except Exception as e:
            print(f'Error al crear respaldo: {e}')

    @staticmethod
    def restaurar_sistema(nombre_archivo: str = 'backups/backup_sistema.pickle') -> list[Usuario] | None:

        ruta_backup = os.path.join(RUTA_BACKUPS, 'backup_sistema.pickle')

        if os.path.exists(ruta_backup):
            try:
                with open(ruta_backup, 'rb') as f:
                    return list[Usuario](pickle.load(f))

            except EOFError:
                return []

        return None