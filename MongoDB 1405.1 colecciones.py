from pymongo import MongoClient
  # conexion
CONEXION = "mongodb+srv://usuario:password@curso.q5vsp6a.mongodb.net/?retryWrites=true&w=majority"
 
   # Usamos MongoClient para conectarnos
cliente = MongoClient(CONEXION)
 
# Creamos la Base de datos      use db1
dbname=cliente['db1']
dbname=cliente.db1
print(dbname)