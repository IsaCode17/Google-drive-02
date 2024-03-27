import requests
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Autenticación con Google Drive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Esto abrirá una ventana en tu navegador para autenticarte

# Crear un cliente de Google Drive
drive = GoogleDrive(gauth)

# URL del archivo que quieres subir
url_archivo = 'URL_del_archivo_remoto'

# Descargar el archivo temporalmente
nombre_archivo = 'archivo_temporal.txt'
r = requests.get(url_archivo)
with open(nombre_archivo, 'wb') as f:
    f.write(r.content)

# Crear un objeto de archivo en Google Drive
archivo_drive = drive.CreateFile({'title': nombre_archivo})

# Establecer el contenido del archivo
archivo_drive.SetContentFile(nombre_archivo)

# Subir el archivo
archivo_drive.Upload()

print("Archivo subido exitosamente a Google Drive.")

# Eliminar el archivo temporal
os.remove(nombre_archivo)
