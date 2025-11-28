# Backend main API file
from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def home(): return {'status':'backend running'}