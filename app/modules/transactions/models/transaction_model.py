from app.base.Model import Model

class Transaction(Model):
    def __init__(self, name: str, description: str, transaciton_type: bool, userId: str):
        super().__init__()
        self.name = name
        self.description = description,
        self.transaction_type = transaciton_type
        self.userId = userId

    def toDict(self) -> dict[str, any]:
        return {
            "name": self.name,
            "description": self.description,
            "transaction_type": self.transaction_type,
            "userId": self.userId,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

