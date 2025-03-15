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

# id del documento a buscar 
documento={"_id": "10009999"}


# buscar  documento
resultado=propiedades.find_one(documento)

# impimir resultado

pprint.pprint(resultado)
pprint.pprint(resultado['summary'])
pprint.pprint(resultado['property_type'])