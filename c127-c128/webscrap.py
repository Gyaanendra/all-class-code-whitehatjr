from bs4 import BeautifulSoup 
from selenium import webdriver 
import time
import csv

starturl = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("F:/api/c127-c128/venv/chromedriver.exe")

browser.get(starturl)
time.sleep(10)

def scrapper():
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    planet_data = []
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
            planet_data.append(temp_list)
        # to click on the next button
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    # to write the data in a new csv file 
    with open("data2_c128.csv",'w')as future_data:
        future_data_writter = csv.writer(future_data)
        future_data_writter.writerow(headers)
        future_data_writter.writerows(planet_data)
      
            
        
scrapper()        
