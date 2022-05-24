import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

f = open('news.csv', 'w', encoding='UTF-8_sig', newline='\n')
file = csv.writer(f)
file.writerow(['Category', 'Title', 'text', 'Image URL'])

for ind in range(1, 6):
    url = 'http://exclusivenews.ge/post/category/msoflio/page/' + str(ind)
    r = requests.get(url)
    print(r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    section = soup.find('section', class_='small-12 medium-8 columns equal')
    news = section.find_all('article')
    for each in news:
        category = each.aside.a.text
        title = each.header.h5.a.text
        text = each.p.text
        image_url = each.img.attrs.get('src')
        # print(category)
        # print(title)
        # print(text)
        # print(image_url)
        file.writerow([category, title, text, image_url])
    sleep(randint(15, 20))

f.close()