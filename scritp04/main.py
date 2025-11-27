import os
from dotenv import load_dotenv
import requests

# Cargar el archivo .env
load_dotenv()

API_URL = os.getenv("API_URL")

def llamar_api():
    response = requests.get(API_URL)
    datos = response.json()
    print(datos)

if __name__ == "__main__":
    llamar_api()