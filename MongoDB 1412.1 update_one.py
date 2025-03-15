from pymongo import MongoClient
import pprint
  # conexion
CONEXION_LOCAL="mongodb://admin:lepanto@localhost"
CONEXION_ATLAS = "mongodb+srv://admin:lepanto@cluster0.1jkwhhs.mongodb.net/?retryWrites=true&w=majority"
 
   # Usamos MongoClient para conectarnos
cliente = MongoClient(CONEXION_ATLAS)
 
# Accedemos a la base de datos
dbname=cliente['sample_airbnb']

# Coleccion a usar
propiedades=dbname['listingsAndReviews']

# Documento a modificar
documento={"_id":"10006546"}

# Cambio a realizar poner noches minimas a 1
cambio={"$set":{"minimum_nights":1}}

# modificar documento
resultado=propiedades.update_one(documento,cambio)

#Identificar los documentos localizados y los modificados
pprint.pprint(resultado.matched_count)
pprint.pprint(resultado.modified_count)

pprint.pprint(propiedades.find_one(documento)["minimum_nights"])