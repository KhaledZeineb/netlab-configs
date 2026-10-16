import os
import requests
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("DEVICE_HOST")
USER = os.getenv("DEVICE_USER")
PASSWORD = os.getenv("DEVICE_PASSWORD")

BASE_URL = f"http://{HOST}/rest"
AUTH = (USER, PASSWORD)

# Modifier le commentaire de l'adresse sur ether2
response = requests.patch(
    f"{BASE_URL}/ip/address/*2",
    auth=AUTH,
    json={"comment": "Adresse configuree via API REST"},
    timeout=10
)

print("Code HTTP :", response.status_code)
print("Détail MikroTik :", response.text)
response.raise_for_status()

print("Commentaire modifié avec succès.")