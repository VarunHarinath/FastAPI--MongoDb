from fastapi import FastAPI
from utils.MongoConnection import mongo_db_connection
from routes.route import router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    mongo_db_connection('mongodb://localhost:27017/')

app.include_router(router)