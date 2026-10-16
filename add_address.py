import os
import requests
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("DEVICE_HOST")
USER = os.getenv("DEVICE_USER")
PASSWORD = os.getenv("DEVICE_PASSWORD")

BASE_URL = f"http://{HOST}/rest"
AUTH = (USER, PASSWORD)

# Vérifier si l'adresse existe déjà
response = requests.get(
    f"{BASE_URL}/ip/address",
    auth=AUTH,
    timeout=10
)
response.raise_for_status()

addresses = response.json()

already_exists = any(
    item.get("address") == "192.168.20.1/24"
    and item.get("interface") == "ether2"
    for item in addresses
)

if already_exists:
    print("L'adresse existe déjà sur ether2.")
else:
    response = requests.put(
        f"{BASE_URL}/ip/address",
        auth=AUTH,
        json={
            "address": "192.168.20.1/24",
            "interface": "ether2",
            "comment": "TP API REST"
        },
        timeout=10
    )
    print("Code HTTP :", response.status_code)
    print("Détail MikroTik :", response.text)
    response.raise_for_status()