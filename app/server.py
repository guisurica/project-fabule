from fastapi import FastAPI
from config.config import settings
from app.modules.transactions.routes import transaction_routes

app = FastAPI()


app.include_router(prefix="/transactions", router=transaction_routes.router)

@app.get("/root")
def root():
    return {
        "environment": settings.ENVIRONMENT
    }