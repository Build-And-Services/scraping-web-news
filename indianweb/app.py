import requests
from bs4 import BeautifulSoup
import openpyxl


keyword = [
  "https://timesofindia.indiatimes.com/topic/sports-event-for-air-polution/news",
  "https://timesofindia.indiatimes.com/topic/air-quality-for-sports/news",
]

# Membuat workbook baru
workbook = openpyxl.Workbook()
sheet = workbook.active

sheet.append(["Source", "Theme", "Publish Date", "Area Covered", "Types of Article"])

checkDuplicate = []

number = 1
for url in keyword:
  for i in range(1, 11):  

    urlTemp = url
    if i > 1:
      urlTemp = url + '/' + str(i)

    resp = requests.get(urlTemp)
    soup = BeautifulSoup(resp.text, 'html.parser')

    card_news = soup.find_all('div', class_="uwU81")
    for item in card_news:
      link = item.find('a')
      date = item.find("div", class_="ZxBIG")
      title = item.find('div', class_="fHv_i o58kM")
      if not(link["href"] in checkDuplicate):
        sheet.append([link["href"],  title.text, date.text.split('/')[-1].split('(')[0].strip(), "", "Reports"])
        checkDuplicate.append(link["href"])
        print("Data news", number, " saved to excel")
        number += 1

excel_file = "output/indianweb.xlsx"
workbook.save(excel_file)