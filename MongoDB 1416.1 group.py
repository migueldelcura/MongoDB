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

# Vamos a agrupar por tipo de Propiedad y averiguar el precio medio
grupo={"$group": {"_id": "$property_type","precio_medio": {"$avg":"$price"}}}

# Crear la tuberia
tuberia=[grupo]

# Lanzar el aggregate
resultados=propiedades.aggregate(tuberia)

# Visualizar el resultado
for elemento in resultados:
   # pprint.pprint(elemento)
    print(elemento['_id']+"  "+str(elemento['precio_medio'])){"threads":[{"position":0,"start":0,"end":421,"connection":"idle"},{"position":422,"start":422,"end":842,"connection":"open"}],"url":"https://att-c.udemycdn.com/2023-06-20_15-44-43-1b9b97a6fb925476fc3cbe9eeb83de9c/original.py?response-content-disposition=attachment%3B+filename%3Dgroup.py&Expires=1710754105&Signature=KTVE77x05uMJ2YFrqRjIZkPtIAbigj29epZw-qkXrh81yOGQEtL5f1Ntd3VYJyIHkQw0BHhJCPrC-E-LAYmhrv2R8feKsJQeLB-YZ78slXvlcvOJ9xE3tRUrbKZk3l8MxKoG8npT4cNNlHtuYPjd212H9rHyKXlKWhtZdu8ljxwukDPjWEtJrca~W0sIKMbvj6GJy0JRZFFxWyhQB7dJEFhonYbhOA6P-DgGq2raRwle-pqcPy63A~Q65J0n0Du9ZSAku5Kq0afVm6-1b-dPls-baXmM4QR82ybfuUvQgNu895HcY54VjnvxKShorFVAutrAlNhhJpkrA3VehgOsJw__&Key-Pair-Id=K3MG148K9RIRF4","method":"GET","port":443,"downloadSize":842,"headers":{"content-type":"binary/octet-stream","content-length":"842","connection":"close","date":"Mon, 18 Mar 2024 05:02:02 GMT","x-amz-replication-status":"COMPLETED","last-modified":"Tue, 20 Jun 2023 15:44:44 GMT","etag":"\"ee7e5ceae4bfd82736885b543989b307\"","x-amz-server-side-encryption":"AES256","x-amz-meta-qqfilename":"group.py","x-amz-version-id":"SrLEUqnCDq1GuBCFmyBwYLfTpAIDN9OZ","content-disposition":"attachment; filename=group.py","accept-ranges":"bytes","server":"AmazonS3","x-cache":"Miss from cloudfront","via":"1.1 3c13cc51908e4d37d2a5046d7703e256.cloudfront.net (CloudFront)","x-amz-cf-pop":"FRA56-P10","x-amz-cf-id":"-jTomIwgGdpvY9LNt4ssUIyLj4XaMPwA8FMj9hs-NRUeDyP1QJ_XAA==","x-cdn":"cf-cloudfront","vary":"Origin"}}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              