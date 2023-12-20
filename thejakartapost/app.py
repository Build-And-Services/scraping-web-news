from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os
import openpyxl

driver = webdriver.Edge()


# Membuat workbook baru
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.append(["Source", "Theme", "Publish Date", "Area Covered", "Types of Article"])
excel_file = "jakartapost.xlsx"

keyword = ['Air Pollution Sport', 'Air Quality Sport']
for key in keyword:
    url = "https://www.thejakartapost.com/search?q="+key+"#gsc.tab=0&gsc.q=air%20pollution&gsc.page="
    urlNews = []
    for i in range(1,11):
        driver.get(url+str(i))

        # Ambil konten dari halaman
        page_content = driver.page_source

        # Tampilkan atau simpan konten sesuai kebutuhan
        soup = BeautifulSoup(page_content, 'html.parser')

        # Temukan semua elemen dengan class "gs-title"
        gs_title_elements = soup.find_all(class_="gs-title")

        # Loop melalui elemen-elemen dan ambil atribut href
        for gs_title_element in gs_title_elements:
            link = gs_title_element.find('a')
            if link:
                href = link.get('href')
                if href in urlNews or str(href) == 'None':
                    pass
                else:
                    urlNews.append(href)

    for link in urlNews:
            driver.get(link)

            # Ambil konten dari halaman
            page_content = driver.page_source

            # Tampilkan atau simpan konten sesuai kebutuhan
            soup = BeautifulSoup(page_content, 'html.parser')

            theme = soup.find('h1',class_="title-large")
            posting = soup.find('div',class_="post-like")
            areaHtml = soup.find('span',class_="posting")
            date = soup.find('span',class_="day")
            if theme != None and posting != None and areaHtml != None and date != None:
                area = areaHtml.get_text(strip=True).split()

                sheet.append([link,theme.get_text(), date.get_text(), " ".join(area[:2]),'Report'])
                workbook.save(excel_file)


driver.quit()