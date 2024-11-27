from pydantic import BaseModel
from typing import List, Optional


class Jcasc(BaseModel):
    allowsSignup:bool = True
    allowAnonymousRead:bool = True
    cache_size:int = 1
    executators:int = 1
    required_plugins:List[str]
    