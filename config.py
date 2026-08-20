import os 
from dotenv import load_dotenv

load_dotenv()

BASE_URL_API = os.getenv("BASE_URL_API")

DB_URL = (
    f"postgresql+psycopg://"
    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)
#DB_URL = os.getenv("DB_URL")

print(f"Connecting to: {DB_URL}")