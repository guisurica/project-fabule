from config.db.db_functions import Connection
from app.server import settings
from ..models.transaction_model import Transaction
from ..dtos.Create_transaction_dto import CreateTransactionDTO
from app.base.Result import Result

async def create_transaction(input: CreateTransactionDTO) -> Result:
    connection = Connection(settings.DB_NAME, "transactions")
    await connection.start_connection()
    collection = await connection.get_collection()
    result = Result()

    if not input.description:
        return result.not_ok_result("Description is required", 400)

    if not input.type:
        return result.not_ok_result("Type is required", 400)
    
    if not input.userId:
        return result.not_ok_result("Transaction need a user", 400)
    
    if not input.name:
        return result.not_ok_result("Name is required", 400)

    new_transaction = Transaction(
        name=input.name,
        description=input.description,
        transaciton_type=input.type,
        userId=input.userId
    )

    try:
        collection.insert_one(new_transaction)
        await connection.close_connection()
        return result.ok_result("Created successfully", 200)
    except Exception:
        await connection.close_connection()
        return result.not_ok_result("Something happened, try again latter. If the problem persists call support", 500)
    
