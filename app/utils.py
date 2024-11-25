
import os
from fastapi import HTTPException
from pymongo import MongoClient,ASCENDING,errors

def get_mongo_client():

    client = MongoClient(host=os.environ.get('MONGO_HOST'),
                            port=int(os.environ.get('MONGO_PORT')),
                            username=os.environ.get('MONGO_INITDB_ROOT_USERNAME'), 
                            password=os.environ.get('MONGO_INITDB_ROOT_PASSWORD'))
    
    return client



def get_mongo_collection(col:str):

    client = get_mongo_client()
    col = client[os.environ.get('MONGO_INITDB_DATABASE')][col]
    return col
        
        
def save_to_mongo(data:dict,index:str,collection:str) -> None:
    
    try:

        col = get_mongo_collection(collection)

        col.create_index(index, unique=True)
        
        col.insert_one(data)

    except errors.DuplicateKeyError:

        pass


