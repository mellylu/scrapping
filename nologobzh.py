import requests
from bs4 import BeautifulSoup
import json

# url="https://www.lenormandy.net/agenda/"
url = "https://www.nologobzh.com/programmation-2023/"
response = requests.get(url)

if response.status_code == 200:
    with open('nologobzh.json') as mon_fichier:
        data = json.load(mon_fichier)

    soup = BeautifulSoup(response.content, "html.parser")
    logo = soup.find('img').get('src') #image logo
    print(logo)
    data.append({"src_logo":logo})
    tab=[]

    for wrapper in soup.find_all('div', class_="nlbzh-thumb-overlay-txt artistes fadeIn-left"):
        h2 = wrapper.find('h2')
        premier_paragraphe = wrapper.find('p')
        p = wrapper.find_all('p')
        deuxieme_paragraphe = p[1]
        date = "pas défini"
        if (deuxieme_paragraphe.text.split(" / ")[0]):
            date=deuxieme_paragraphe.text.split(" / ")[0]

            # Supprimer les espaces au début et à la fin et décoder la chaîne
            date = date.strip().encode('latin-1', 'replace').decode('latin-1')
            

            # Afficher le résultat
            # print(chaine_formatee)

        # print(deuxieme_paragraphe.text.split(" / ")[2])
        # deuxieme_paragraphe.text.split(" / ")[0]
        # print(deuxieme_paragraphe.text)
        # for text in p:
        #     print(text.text)
    
        # print(p.text)
        # print(deuxieme_paragraphe.text)



        #bon
        
        obj_prog={"nom_artiste":h2.text, "pays":premier_paragraphe.text, "date":date}
        tab.append(obj_prog)
        #fin bon
        
        # y = json.loads(x)
    
    


    #bon
    obj_prog={'programmation':tab}
    # print(obj_prog)
    data.append(obj_prog)
    #fin bon


        # tab.append(wrapper.text)
    # print(tab)


    #bon
    file = open('nologobzh.json', 'w')
    file.write(json.dumps(data))
    file.close()
    #fin bon













    # soup = BeautifulSoup(response.content, "html.parser")
    # p = soup.find_all('div', class_="gig-date")
    # # contenu = p.text
    # # for wrapper in soup.find_all('div', class_="gig-date"):
    #     # print(wrapper.text)
    # # print(contenu)
    
   
    # programmation = soup.find_all('article', class_="idcalendar-eventcard bloc-news bloc-events saison ")

    # programmation = soup.find("a").get('href')
    # # print(soup.select('div > h2'))

    # for wrapper in programmation:
    #     print(wrapper.text)
    

    # print(programmation)

#     ma_div = soup.find('div', class_=re.compile(r'\bartistes\b'))

# # Récupérer le texte à l'intérieur de la balise div
#     # contenu = ma_div.text
#     # programmation1 = soup.find('a', "h2") 
#     # ma_div = soup.find_all("div", class_="nlbzh-thumb-overlay-txt artistes fadeIn-left")
    
#     # print(ma_div)
#     programmation1 = soup.find('div', class_='nlbzh-thumb-overlay-txt artistes fadeIn-left')#.findAll('h2')
    # print(programmation1)
    # print(paragraphs)
    # for paragraph in paragraphs:
    #     print("hhhhh")
    #     print(paragraph.text)