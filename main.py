from fastapi import FastAPI
from typing import Optional
from routes import auth
from fastapi.middleware.cors import CORSMiddleware
from middlewares.auth import AuthMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True, 
    allow_methods=['*'],
    allow_headers=['*']

    )
app.add_middleware(AuthMiddleware)

app.include_router(auth.router, tags='Auth', prefix='/api/v1')
@app.get('/health')
def health_check():
    return {
        'status':'ok'
    }