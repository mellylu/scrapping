import requests
from bs4 import BeautifulSoup
import json

url = "https://www.nologobzh.com/programmation-2023/"
response = requests.get(url)

if response.status_code == 200:
    data=[]
    file = open('nologobzh.json', 'w')
    file.write(json.dumps(data))
    file.close()
    with open('nologobzh.json') as mon_fichier:
        data = json.load(mon_fichier)

    soup = BeautifulSoup(response.content, "html.parser")
    logo = soup.find('img').get('src')
    data.append({"src_logo":logo})
    tab=[]

    for wrapper in soup.find_all('div', class_="nlbzh-thumb-overlay-txt artistes fadeIn-left"):
        h2 = wrapper.find('h2')
        premier_paragraphe = wrapper.find('p')
        p = wrapper.find_all('p')
        deuxieme_paragraphe = p[1]
        date = "pas défini"
        scene = "pas défini"
        
        if (deuxieme_paragraphe.text.split(" / ")[0]):
            date=deuxieme_paragraphe.text.split(" / ")[0]
            date = date.strip().encode('latin-1', 'replace').decode('latin-1')
        if (deuxieme_paragraphe.text.split(" / ")[1]):
            scene = deuxieme_paragraphe.text.split(" / ")[1]
            scene = scene.strip().encode('latin-1', 'replace').decode('latin-1')
        try:
            troisieme_partie = deuxieme_paragraphe.text.split(" / ")[2]
            horaire = deuxieme_paragraphe.text.split(" / ")[2]
            horaire = horaire.strip().encode('latin-1', 'replace').decode('latin-1')
        except IndexError:
            horaire = "pas défini"

        obj_prog={"nom_artiste":h2.text, "pays":premier_paragraphe.text, "date":date, "scene":scene, "horaire":horaire}
        tab.append(obj_prog)
    
   
    obj_prog={'programmation':tab}
    data.append(obj_prog)

    normalized_data = json.loads(json.dumps(data, ensure_ascii=False))

    with open('nologobzh.json', 'w', encoding='utf-8') as file:
        json.dump(normalized_data, file, ensure_ascii=False, indent=2)
