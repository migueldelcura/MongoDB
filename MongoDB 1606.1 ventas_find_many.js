//Importar el cliente MongoDB
const mongo=require('mongodb').MongoClient

//conexion
const conexion_local="mongodb://admin:lepanto@127.0.0.1"
const conexion_atlas = "mongodb+srv://user:pass@tu_cluster.mongodb.net/?retryWrites=true&w=majority"

//Establecer una conexion con Mongo
const cliente=new mongo(conexion_local)

//indicar Base de datos
const dbname="db1";
//Indicar la coleccion
const coleccion="ventas"

//Crear una variable que apunte a la conexión
const ventas=cliente.db(dbname).collection(coleccion)

// Crear el filtro
consulta={ cod_cliente: {"$gt": 200}}

// Nos conectamos a a la Base de Datso

const main= async() => {
  try {
      //Conectarnos a mongo
      await cliente.connect();
      console.log(`He conseguido conectarme a mongo con la cadena ${conexion_local}`)
      let resultado= await ventas.find(consulta)
      console.log(`He conseguido conectar a ${dbname} y buscar varios documentos en ${coleccion}`)
      // contar documentos
      console.log(`He encontrado ${ await ventas.countDocuments(consulta)}`)
      // Recorrer el cursor
      //for await (const documento of resultado) { console.log(documento)}
      for await (const documento of resultado) { console.log(documento.nombre)}


  } catch (fallo) {
    console.error(`He tenido un problema en la operacion ${fallo}`)    
  } finally {
      await cliente.close()
  }


};

main();

