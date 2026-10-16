import os
import requests
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("DEVICE_HOST")
USER = os.getenv("DEVICE_USER")
PASSWORD = os.getenv("DEVICE_PASSWORD")

BASE_URL = f"http://{HOST}/rest"
AUTH = (USER, PASSWORD)

# Paramètres de la route de test
DESTINATION = "10.10.10.0/24"
GATEWAY = "192.168.93.2"

# Lire les routes existantes
response = requests.get(
    f"{BASE_URL}/ip/route",
    auth=AUTH,
    timeout=10
)
response.raise_for_status()

routes = response.json()

# Vérifier si la route existe déjà
route_exists = any(
    route.get("dst-address") == DESTINATION
    and route.get("gateway") == GATEWAY
    for route in routes
)

if route_exists:
    print("La route existe déjà : aucun changement.")
else:
    response = requests.put(
        f"{BASE_URL}/ip/route",
        auth=AUTH,
        json={
            "dst-address": DESTINATION,
            "gateway": GATEWAY,
            "comment": "TP API REST - route de test"
        },
        timeout=10
    )

    print("Code HTTP :", response.status_code)
    print("Détail MikroTik :", response.text)
    response.raise_for_status()

    print("Route statique ajoutée avec succès.")