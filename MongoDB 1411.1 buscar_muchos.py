from pymongo import MongoClient
import pprint
  # conexion
CONEXION_LOCAL="mongodb://admin:lepanto@localhost"
CONEXION_ATLAS = "mongodb+srv://admin:lepanto@curso.q5vsp6a.mongodb.net/?retryWrites=true&w=majority"
 
   # Usamos MongoClient para conectarnos
cliente = MongoClient(CONEXION_ATLAS)
 
# Accedemos a la base de datos
dbname=cliente['sample_airbnb']

# Coleccion a usar
propiedades=dbname['listingsAndReviews']

# Documentos a buscar, mas de 3 dormitorios
documentos={ "bedrooms": {"$gt": 3}  }

# buscar  documento

resultados=propiedades.find(documentos)

# impimir resultado. Solo _id y nombre
for resultado in resultados:
    pprint.pprint(resultado['_id']+" "+resultado['name'])
