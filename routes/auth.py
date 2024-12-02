from datetime import datetime
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from db import db
from models import User
from serializers.user import user_serializer
from utils.jwt_token import create_token

router = APIRouter()

class UpdateUser(BaseModel):
    name: str
    phone: str

@router.post('/auth/update-user')
async def update_user(request: UpdateUser):
    # Find the user in the database
    user = await db.get_collection('users').find_one({'phone': request.phone})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update the user's name
    result = await db.get_collection('users').update_one(
        {'phone': request.phone}, {'$set': {'name': request.name}}
    )

    if result.modified_count == 0:
        raise HTTPException(status_code=400, detail="No changes made")

    # Fetch the updated user
    updated_user = await db.get_collection('users').find_one({'phone': request.phone})
    response_data =  {'message': 'User updated successfully', 'user': user_serializer(updated_user)}
    return JSONResponse(response_data,status_code=201)


@router.post('/auth')
async def auth(phone: str):
    user = await db.get_collection('users').find_one({'phone': phone})
    if not user:
        user = {
            'phone': phone,
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }
        result = await db.get_collection('users').insert_one(user)
        user['_id'] = result.inserted_id 
    
    user = user_serializer(user)
    token = create_token(user)
    return JSONResponse({
        'token':token,
        'user':user
    },status_code=201)
