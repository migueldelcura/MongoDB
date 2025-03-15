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

# Documentos a modificar, todos los que tengan dos dormitorios
documentos={"bedrooms": 2}

# Cambio a realizar poner dormitorios a 22.
cambio={"$inc": {"bedrooms": 20}}

# modificar documento
resultado=propiedades.update_many(documentos,cambio)

#Identificar los documentos localizados y los modificados
pprint.pprint(resultado.matched_count)
pprint.pprint(resultado.modified_count)