from typing import List, Optional
from bson import ObjectId
from pydantic import BaseModel, Field
from datetime import datetime
from .Nextform import NextForm
class User(BaseModel):
    phone: str
    name: Optional[str] = None
    email: Optional[str] = None
    created_at: datetime
    updated_at:datetime
    nextform: Optional[List[NextForm]]
    id: Optional[str] = Field(None, alias='_id')

    class Config:
        json_encoders = {
            ObjectId: str,
            datetime: lambda dt: dt.timestamp()

        }

