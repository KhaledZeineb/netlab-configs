
import os
import requests
import urllib3
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("DEVICE_HOST")
USER = os.getenv("DEVICE_USER")
PASSWORD = os.getenv("DEVICE_PASSWORD")

BASE_URL = f"http://{HOST}/rest"
AUTH = (USER, PASSWORD)

# Désactive les avertissements TLS uniquement si HTTPS est utilisé
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

try:
    response = requests.get(
        f"{BASE_URL}/ip/address",
        auth=AUTH,
        timeout=10
    )
    response.raise_for_status()
    print("Adresses IP du routeur :")
    print(response.json())

except requests.exceptions.RequestException as error:
    print("Erreur de connexion à MikroTik :", error)
