from pymongo import MongoClient
import pprint
  # conexion
CONEXION_LOCAL="mongodb://admin:lepanto@localhost"
CONEXION_ATLAS = "mongodb+srv://admin:lepanto@cluster0.1jkwhhs.mongodb.net/?retryWrites=true&w=majority"
 
   # Usamos MongoClient para conectarnos
cliente = MongoClient(CONEXION_LOCAL)
 
# Accedemos a la base de datos
dbname=cliente['db1']

# Coleccion a usar
libros=dbname['libros']

# Documentos a borrar. Los de la editorial Terra
documentos= {"editorial": "Terra"}

# eliminar documentos
resultado=libros.delete_many(documentos)

#Identificar los documentos  borrados
print(resultado.deleted_count)