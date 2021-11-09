import requests
from bs4 import BeautifulSoup
import time


date_now = time.strftime("%d.%m.%Y")
base_url = "https://63.ru"

full_url = f"{base_url}/search/?keywords=covid&sort=date&dateFrom={date_now}&dateTo={date_now}"
response = requests.get(full_url)

# Получаем весь код страницы
soup = BeautifulSoup(response.content, "lxml")
# Вытаскиваем интересующую нас информацию с помощью элементов и их атрибутов
teme = soup.find_all("h2", class_="GNjj")
for title in teme:
    print(title.text)
    href = title.find("a", {"data-test" :"archive-record-header"}).get("href")
    print(base_url + href)
    print("===================================================")
   

