from selenium import webdriver
from bs4 import BeautifulSoup
import json
import csv, time

driver = webdriver.Edge()


driver.get('https://www.dw.com/search/?languageCode=en&item=sport%20event%20for%20reduce%20air%20pollution%20&contentType=ARTICLE&searchNavigationId=9097-30688&sort=RELEVANCE&resultsCounter=350')

page_content = driver.page_source
html_response = BeautifulSoup(page_content, 'html.parser')
html_link = html_response.find_all('div', class_='searchResult')
data = []
linnks = []
item = [

]
no = 1
for i in html_link:
  link = i.find('a')['href']
  driver.get('https://dw.com'+link)

  time.sleep(3)
  page_content = driver.page_source
  html_response = BeautifulSoup(page_content, 'html.parser')

  header = html_response.find('header')
  if header == None:
     continue
  judul = header.find('h1').text
  encoded_text = judul.encode('ascii', 'ignore')


  publish = html_response.find('span', class_="publication")
  publish = publish.find("time").text

  country = html_response.find('div', class_="kicker")
  country = country.find_all("span")
  if(len(country) >= 2):
    item.append(["https://dw.com"+link,encoded_text.decode('ascii'), publish, country[1].text])
  else:
    item.append(["https://dw.com"+link,encoded_text.decode('ascii'), publish, ''])


with open("dw-news.csv", mode='w', newline='') as csv_file:
  writer = csv.writer(csv_file)
  for d in item:
    writer.writerow(d)


driver.quit()