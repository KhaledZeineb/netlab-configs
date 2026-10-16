\# TP — API REST MikroTik RouterOS v7



\## 1. Objectif



Configurer un routeur MikroTik RouterOS v7 depuis Python en utilisant l'API REST.



\## 2. Environnement



\- Routeur : MikroTik CHR

\- Version RouterOS : 7.24.5

\- Langage : Python

\- Bibliothèques : `requests`, `python-dotenv`

\- Authentification : utilisateur API dédié



\## 3. Configuration



Les paramètres de connexion sont stockés dans le fichier `.env` :



\- `DEVICE\_HOST`

\- `DEVICE\_USER`

\- `DEVICE\_PASSWORD`



Le fichier `.env` ne doit jamais être envoyé sur GitHub.



\## 4. Opérations API REST réalisées



\- GET : récupérer les adresses IP du routeur.

\- PUT : ajouter l'adresse `192.168.20.1/24` sur `ether2`.

\- PATCH : modifier le commentaire de cette adresse.

\- DELETE : supprimer l'adresse de test.



\## 5. Route statique idempotente



Le script `configure\_route.py` vérifie les routes existantes avant d'ajouter la route de test :



\- Destination : `10.10.10.0/24`

\- Passerelle : `192.168.93.2`



La première exécution a créé la route avec le code HTTP 201. La deuxième exécution a détecté la route existante et n'a pas créé de doublon.



\## 6. Scripts



\- `read\_addresses.py` : lecture des adresses IP.

\- `add\_address.py` : ajout d'une adresse IP.

\- `update\_address.py` : modification du commentaire.

\- `delete\_address.py` : suppression de l'adresse de test.

\- `configure\_route.py` : configuration idempotente d'une route.



\## 7. Sécurité



\- Ne pas publier les identifiants.

\- Exclure `.env` de Git avec `.gitignore`.

\- Utiliser HTTPS avec un certificat correctement configuré dans un environnement réel.

\- Limiter les permissions du compte API au strict nécessaire.



