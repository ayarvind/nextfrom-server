from models import User


def user_serializer(user:User)->dict:

    return{
        'phone': user['phone'],
        'name': user.get('name'),  
        'email': user.get('email'), 
        'created_at': user.get('created_at').isoformat() if user.get('created_at') else None,
        'updated_at': user.get('updated_at').isoformat() if user.get('updated_at') else None,
        'id': str(user['_id'])  
    }