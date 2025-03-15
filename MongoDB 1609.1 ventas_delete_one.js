//Importar el cliente MongoDB
const mongo= require('mongodb').MongoClient;


// conexion
const conexion_local="mongodb://admin:lepanto@127.0.0.1"
const conexion_atlas = "mongodb+srv://uer:pass@tu_cluster.mongodb.net/?retryWrites=true&w=majority"

// Establezco una nueva conexión con mongo
const cliente=new mongo(conexion_local)

// Indico la Base de Datos
const dbname="db1"

//Indico la colección
const coleccion="ventas"
//Creo una variable que apunt a esa colección
const ventas=cliente.db(dbname).collection(coleccion)

//Creo una query
const consulta={cod_cliente: {"$eq": 400}}


const main= async() => {
    try{
          //Conectarnos a mongo
          await cliente.connect();
          console.log(`He conseguido conectarme a mongo con la cadena ${conexion_local}`)
          let resultado= await ventas.deleteOne(consulta)
          console.log(`He conseguido conectar a ${dbname} y borrar un documento en ${coleccion}`)
          console.log(`He modificado ${resultado.deletedCount} documentos `)
    } catch(fallo){
        console.error(`He tenido un problema en la operación: ${fallo}`)
    } finally {
        await cliente.close()
    }
};

main();

{"threads":[{"position":0,"start":0,"end":607,"connection":"idle"},{"position":608,"start":608,"end":1214,"connection":"open"}],"url":"https://att-c.udemycdn.com/2023-06-22_20-23-31-18bace7ec9f1dca4bf6bd25a3a4bb432/original.js?response-content-disposition=attachment%3B+filename%3Dventas_delete_one.js&Expires=1710754105&Signature=Cw4ueb1cOUEcN3ksLGKvUCa7A2T9l4ErkzRHxm6gSADkL4EkSumw8-QeFDzhAGMBzfpkSA7fmlp4jJtD7ngl0LzceL1Teb4xdZOzbZXR8ktyaPEJiFdjbWqJ18UVcbzZwsbLUZvbgEUmE4R3dGxdMF6xFkQmA7pEQgYWVGKsaBvm--HlDYwhRZ0MDm~9J97onVwGNCiQum77zou-0ild0unaatM1zj3NOJ2xvquWFt4g8GGnBLP~kVdmu8wDopBvo2KsoSoHcTJ-7RmtELg46fqXuViu6Q5BUoCchI1gGWJJAZZkg5rlLpLtCsRItZYwFSBUUeQugkMLNOBvOevKQA__&Key-Pair-Id=K3MG148K9RIRF4","method":"GET","port":443,"downloadSize":1214,"headers":{"content-type":"text/javascript","content-length":"1214","connection":"close","date":"Mon, 18 Mar 2024 05:02:27 GMT","x-amz-replication-status":"COMPLETED","last-modified":"Thu, 22 Jun 2023 20:23:34 GMT","etag":"\"059a9e3beffa0925a422adab469108f2\"","x-amz-server-side-encryption":"AES256","x-amz-meta-qqfilename":"ventas_delete_one.js","x-amz-version-id":"jm4fbCRPJ.qw7OKNzMVBS1W5myffY9ey","content-disposition":"attachment; filename=ventas_delete_one.js","accept-ranges":"bytes","server":"AmazonS3","x-cache":"Miss from cloudfront","via":"1.1 38dab0d877593711162f7409f4fc8fca.cloudfront.net (CloudFront)","x-amz-cf-pop":"FRA56-P10","x-amz-cf-id":"MH8xZx5JwxeRaIR1NPTHoBN2zBEURFFZTOZval1wuAqmDZeC0VjJIg==","x-cdn":"cf-cloudfront","vary":"Origin"}}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           