import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Loan Application API")
VERSION = os.getenv("VERSION", "1.0.0")
DEBUG = os.getenv("DEBUG", "True") == "True"
