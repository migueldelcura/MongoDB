//Importar el cliente MongoDB
const mongo= require('mongodb').MongoClient;


// conexion
const conexion_local="mongodb://admin:lepanto@127.0.0.1"
const conexion_atlas = "mongodb+srv://uer:pass@tu_cluster.mongodb.net/?retryWrites=true&w=majority"

// Establezco una nueva conexión con mongo
const cliente=new mongo(conexion_local)

// Indico la Base de Datos
const dbname="db1"



const main= async() => {
    try{
        // Nos conectamos a MongoDB
        await cliente.connect();
        console.log(`He conseguido conectarme a MongoDB con la cadena ${conexion_local}`)
    } catch(fallo){
        console.error(`He tenido un problema en la operación: ${fallo}`)
    } finally {
        await cliente.close()
    }
};

main();
