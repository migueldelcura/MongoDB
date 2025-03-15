from pymongo import MongoClient
  # conexion
CONEXION_LOCAL="mongodb://admin:lepanto@localhost"
CONEXION_ATLAS = "mongodb+srv://admin:lepanto@curso.q5vsp6a.mongodb.net/?retryWrites=true&w=majority"
 
   # Usamos MongoClient para conectarnos
cliente = MongoClient(CONEXION_LOCAL)
 
# Accedemos a la base de datos
dbname=cliente['db1']

# Coleccion a usar o a crear
# dbname.facturas
facturas=dbname['facturas']   
#Documento a insertar
factura1={
    "cod_factura": 1,
    "descripcion": "Un ejemplo de factura",
    "total": 100,
    "productos": ["tomate","pera","limones"]

}

# Insertar documento
resultado=facturas.insert_one(factura1)

print(resultado)
colecciones=dbname.list_collection_names()

print(colecciones)
for coleccion in colecciones:
    print(coleccion)
