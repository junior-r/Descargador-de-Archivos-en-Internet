from urllib import request

url = input('Ingrese URL del archivo a Descargar: ')
local_path = input('Ingrese la ruta local donde desea Descargar el archivo: ')
name_file = input('Ingrese un nombre para el archivo a Descargar: ')
extension = input('Ingrese la extensión para su archivo: ')
downloaded_file = local_path + '/' + name_file + extension
try:
  request.urlretrieve(url, downloaded_file)
  print(f'Su archivo se descargo exitosamente.\nFue guardado en {downloaded_file}')
except:
  print('Ha ocurrido un error')