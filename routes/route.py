from fastapi import APIRouter
from models.todos import Todo
from config.database import collection
from schema.Schemas import list_serial,indiviual_serial
from bson import ObjectId

router = APIRouter();

# GET method to retrieve all the documents
@router.get('/')
async def get_data():
    todos = list_serial(collection.find())
    return todos

@router.get('/{id}')
async def get_data_by_id(id:str):
    data = collection.find_one({"_id":ObjectId(id)})
    return indiviual_serial(data)

@router.post('/')
async def post_data(todo:Todo):
    collection.insert_one(dict(todo))

@router.put('/{id}')
async def put_data(id:str,todo:Todo):
    
    data = collection.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(todo)})
    return indiviual_serial(data)
    
@router.delete('/{id}')
async def delete_data(id:str):
    collection.find_one_and_update({"_id":ObjectId(id)})
