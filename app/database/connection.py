
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from app.utils import settings

def connect_to_mongo():
    """
    Connect to MongoDB using the provided URI.
    """

    # uri = "mongodb+srv://garima:garima@cluster0.5goe2sc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  
    uri = settings.MONGODB_URI 
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    db = client["Chatbot"]
    appointments_collection = db["Appointments"]
    return appointments_collection

    # Send a ping to confirm a successful connection
    # try:
    #     client.admin.command('ping')
    #     print("Pinged your deployment. You successfully connected to MongoDB!")
    # except Exception as e:
    #     print(e)

if __name__ == "__main__":
    connect_to_mongo()