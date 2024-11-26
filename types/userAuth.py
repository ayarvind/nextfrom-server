from pydantic import BaseModel


class UserAuth(BaseModel):
    phone: str
    # token: str
