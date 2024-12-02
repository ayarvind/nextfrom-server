from datetime import datetime
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel

class NextForm(BaseModel):
    user_id : str
    id : Optional[str]
    name : str
    description : str
    form:Optional[dict]
    created_at : datetime
    updated_at : datetime

    class Config:
        json_encoders = {
            ObjectId:str,
            datetime: lambda dt : dt.timestamp()
        }