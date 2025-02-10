import os 
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

dotenv_file = ".env.development"
#dotenv_file = ".env.production"

print(os.path.exists(dotenv_file))

if os.path.exists(dotenv_file):
    load_dotenv(dotenv_path=dotenv_file)
else:
    raise FileNotFoundError("Erro ao tentar carregar variaveis de ambiente")

class Settings(BaseSettings):
    ENVIRONMENT: str = os.getenv("ENVIRONMENT")
    DB_NAME: str = os.getenv("DB_NAME")

settings = Settings()