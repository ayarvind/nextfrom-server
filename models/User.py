from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field
from datetime import datetime

class User(BaseModel):
    phone: str
    name: Optional[str] = None
    email: Optional[str] = None
    created_at: datetime
    updated_at:datetime
    id: Optional[str] = Field(None, alias='_id')

    class Config:
        json_encoders = {
            ObjectId: str,
            datetime: lambda dt: dt.timestamp()

        }

