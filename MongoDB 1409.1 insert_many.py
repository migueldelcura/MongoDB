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
lista_facturas=[{
    "cod_factura": 2,
    "descripcion": "ejemplo de factura 2",
    "total": 120,
    "productos": ["tomate","manzana","pepinos"]

},
{
    "cod_factura": 3,
    "descripcion": "ejemplo de factura 3",
    "total": 90,
    "productos": ["manzana","fresa"]

},

]
# Insertar documento
resultado=facturas.insert_many(lista_facturas)

print(resultado)
colecciones=dbname.list_collection_names()

print(colecciones)
for coleccion in colecciones:
    print(coleccion)
  