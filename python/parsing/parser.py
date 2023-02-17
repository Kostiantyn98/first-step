import requests
from bs4 import BeautifulSoup 
import csv
from datetime import date, timedelta

CSV = news.csv.


HOST = "https://www.pravda.com.ua/"
URL = "https://www.pravda.com.ua/news/"
HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36"
}

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2013, 1, 1)
end_date = date(2015, 6, 2)
for single_date in daterange(start_date, end_date):
    print(single_date.strftime("%d%m%Y"))

def get_html(url, params=""):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find("div", class_= "war_block")
    news = []
    items = items.find_all("div", class_="war_item")

    for item in items:
        news.append(
            {
            
            "title": item.find("div", class_="war_desc").get_text(strip= True),
            "kol": item.find("div", class_="war_num").get_text(strip= True),
            "card_image":item.find("div", class_="war_img").find("img").get("src")
            }
        )
    return news

def save_doc(items,path):
    with open(path, "w", newline= "") as file:
        writer = csv

def parser():
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        news = []
        for page in range(1, PAGENATION):
            html = get_html(URL, params={"date": page})
            news.extend(get_content(html.text))
        pass
    else:
        print("Error")

parser()