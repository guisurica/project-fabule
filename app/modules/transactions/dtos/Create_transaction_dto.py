from pydantic import BaseModel

class CreateTransactionDTO(BaseModel):
    name: str
    type: bool
    description: str
    userId: str