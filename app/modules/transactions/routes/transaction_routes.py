from fastapi import APIRouter, HTTPException
from ..services.transactions_services import create_transaction
from ..dtos.Create_transaction_dto import CreateTransactionDTO

router = APIRouter()

@router.post("/create")
async def create(input: CreateTransactionDTO):
    result = await create_transaction(input)
    print(f"result {result.message}")
    if not result.ok:
        raise HTTPException(status_code=result.code, detail=result.message)
    return HTTPException(status_code=result.code, detail=result.message)
    


@router.get("/")
async def get_transactions():
    return "imagine there a list of transacitons"