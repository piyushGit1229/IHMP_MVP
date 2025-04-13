from pydantic import BaseModel
from typing import Optional

class PatientBase(BaseModel):
    name: str
    description: Optional[str] = None
