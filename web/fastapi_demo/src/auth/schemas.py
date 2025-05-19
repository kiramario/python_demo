from typing import Optional
from pydantic import BaseModel

class User_Token(BaseModel):
    token: Optional[str]
    token_type: Optional[str] = "Bearer"
