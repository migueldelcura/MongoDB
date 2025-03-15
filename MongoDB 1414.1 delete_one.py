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

# Documento a borrar
documento={"_id": 3}

# eliminar documento
resultado=libros.delete_one(documento)

#Identificar los documentos localizados y los borrados
pprint.pprint(resultado.deleted_count)