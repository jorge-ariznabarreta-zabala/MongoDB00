from ast import Expression
import pymongo

MONGO_HOST="127.0.0.1"
MONGO_PORT="27017"
MONGO_TIMEOUT="1000"

MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PORT+"/"

try:
    cliente=pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIMEOUT)
    cliente.server_info()
    print("Conectado a MongoDB")
    cliente.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo de conexión excedido" +errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print ("*#*#*# Error de conexión *#*#*#" +errorConexion )