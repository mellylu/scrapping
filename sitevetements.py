import requests
from bs4 import BeautifulSoup
import json

total_pages = 5
data=[]

number = 0
for page_number in range(1, total_pages + 1):
    url = "https://aprizo.com/collections/vetements-femme-pas-cher"
    url = url + "?page=" + str(page_number)
    response = requests.get(url)
    html = response.text
    if response.status_code == 200:
        soup = BeautifulSoup(html, 'html.parser')
        tab=[]
        for wrapper in soup.find_all('h3', class_="t4s-product-title"):
            number = number + 1
            tab.append({"nom_article":wrapper.text})
        data.append({'page_number': page_number, 'articles': tab})

        
        with open('sitevetements.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)
    

        

    


