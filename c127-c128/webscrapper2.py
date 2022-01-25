from typing import final
from bs4 import BeautifulSoup 
from selenium import webdriver 
import time
import csv
import requests
starturl = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("F:/api/c127-c128/venv/chromedriver.exe")

browser.get(starturl)
time.sleep(10)

headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude","discovery_date","hyperlink","planet_type","planet_radius","orbital_radius","orbital_period","eccentricity"]
planet_data = []
new_planet_data = []

def new_scrapper(hyperlink):
    for i in range(0,498):
        # while True:
        #     time.sleep(2)
        page = requests.get(hyperlink)
        soup = BeautifulSoup(page.text,"html.parser")
        for tr in soup.find_all("tr",attrs={"class":"fact_row"}):
            td_tag = tr.find_all("td")
            temp_list = []
            for td in td_tag:
                try:
                    temp_list.append(td.find_all("div",attrs={"class":"value"})[0].contents[0])
                except:
                    temp_list.append("")
            new_planet_data.append(temp_list)
            

def scrapper():
    for i in range(0,498):
        soup= BeautifulSoup(browser.page_source,'html.parser')
        for ul in soup.find_all("ul",attrs={"class","exoplanet"}):
            li = ul.find_all("li")
            temp_list = []
            for index,li_tag in enumerate(li):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            hyperlink_li = li[0]
            temp_list.append("https://exoplanets.nasa.gov"+hyperlink_li.find_all("a",href=True)[0]["href"])
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
               
scrapper()     

for h in planet_data:
    new_scrapper(h[5])
    
final_planet_data = []

for index,k in enumerate(planet_data):
    final_planet_data.append(k+final_planet_data[index])
    
with open("data_final_c128.csv",'w')as future_data:
    future_data_writter = csv.writer(future_data)
    future_data_writter.writerow(headers)
    future_data_writter.writerows(final_planet_data)
    

