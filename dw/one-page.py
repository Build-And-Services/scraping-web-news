from selenium import webdriver
from bs4 import BeautifulSoup
import json, csv

driver = webdriver.Edge()


driver.get('https://www.dw.com/en/https-wwwdwcom-en-iran-mens-team-shows-support-for-iranian-women-av-63273202/a-63330579')

item = [

]
page_content = driver.page_source
html_response = BeautifulSoup(page_content, 'html.parser')

header = html_response.find('header')
judul = header.find('h1').text


publish = html_response.find('span', class_="publication")
publish = publish.find("time").text

country = html_response.find('div', class_="kicker")
country = country.find_all("span")
# Menggunakan encode() untuk mengubah string ke bytes
encoded_text = judul.encode('ascii', 'ignore')
print([encoded_text.decode('ascii'), publish,country[1].text])

with open("al.csv", mode='w', newline='') as csv_file:
  writer = csv.writer(csv_file)

  writer.writerow([encoded_text.decode('ascii'), publish,country[1].text])

driver.quit()