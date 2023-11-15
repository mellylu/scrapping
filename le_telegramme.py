import requests
from bs4 import BeautifulSoup
import json

# URL du site à extraire
url = 'https://www.letelegramme.fr/ille-et-vilaine/saint-malo-35400/no-logo-bzh-a-saint-malo-vivement-la-7e-edition-6410481.php'

# Envoi d'une requête HTTP au site
response = requests.get(url)

# Vérification que la requête a réussi
if response.status_code == 200:
    # Analyse du contenu HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Exemple : extraction de tous les paragraphes
    paragraphs = soup.find_all('p')

    data = [{'text': paragraph.text} for paragraph in paragraphs]

    json_data = json.dumps(data, indent=4)

    with open('le_telegramme.json', 'w') as file:
        file.write(json_data)


else:
    print(f"Erreur lors de la récupération du site : {response.status_code}")
