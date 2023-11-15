import requests
from bs4 import BeautifulSoup

url = "https://www.nologobzh.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    paragraphs = soup.find_all('img')
    # print(paragraphs)
    for paragraph in paragraphs:
        print("hhhhh")
        print(paragraph.text)