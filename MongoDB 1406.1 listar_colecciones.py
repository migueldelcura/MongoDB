from pymongo import MongoClient
  # conexion
CONEXION_LOCAL="mongodb://admin:lepanto@localhost"
CONEXION_ATLAS = "mongodb+srv://admin:lepanto@curso.q5vsp6a.mongodb.net/?retryWrites=true&w=majority"
 
   # Usamos MongoClient para conectarnos
cliente = MongoClient(CONEXION_LOCAL)
 
# Creamos la Base de datos      use db1
dbname=cliente['db1']

colecciones=dbname.list_collection_names()

print(colecciones)
for coleccion in colecciones:
    print(coleccion)