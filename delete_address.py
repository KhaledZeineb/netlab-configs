import os
import requests
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("DEVICE_HOST")
USER = os.getenv("DEVICE_USER")
PASSWORD = os.getenv("DEVICE_PASSWORD")

BASE_URL = f"http://{HOST}/rest"
AUTH = (USER, PASSWORD)

response = requests.delete(
    f"{BASE_URL}/ip/address/*2",
    auth=AUTH,
    timeout=10
)

print("Code HTTP :", response.status_code)
print("Détail MikroTik :", response.text)
response.raise_for_status()

print("Adresse IP supprimée avec succès.")