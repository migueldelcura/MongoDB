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
          console.log(`He borrado ${resultado.deletedCount} documentos `)
    } catch(fallo){
        console.error(`He tenido un problema en la operación: ${fallo}`)
    } finally {
        await cliente.close()
    }
};

main();