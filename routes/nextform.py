from fastapi import APIRouter, Request
from pydantic import BaseModel
from db import db
from models import User
router = APIRouter()

class NextFormType(BaseModel):
    name : str
    description : str

@router.post('/nextform')
async def create_form(request:Request):
    form_meta_data:NextFormType = request.body
    user = User( request.headers.get('x-auth-key'))
    new_form = await db.get_collection('nextforms').insert_one({
        'user_id' : user.id,
        'name' : form_meta_data.name,
        'description': form_meta_data.description 
    })

