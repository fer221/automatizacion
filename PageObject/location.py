from selenium import webdriver
from selenium.webdriver.common.by import By
from HomePage import HomePage
from HomePage import base_url
import pathlib
import csv



driver = webdriver.Chrome()
driver.get(base_url)

search_type = driver.find_element(*HomePage.ingreso)
search_type.send_keys("camisetas")

click_search = driver.find_element(*HomePage.click)
click_search.click()


articulo = []
div_father = driver.find_elements(*HomePage.div_tshirt)

frist_name = div_father[0].find_element_by_xpath("//div[@class='ui-search-item__group ui-search-item__group--title']//h2")
conv_frist_name = frist_name.text
link_father = div_father[0].find_element_by_xpath("//div[@class='ui-search-item__group ui-search-item__group--title']//a")
link = link_father.get_attribute("href")

price = div_father[0].find_element_by_xpath("//div[@class='ui-search-price__second-line']//span")
conv_price = price.text

articulo.append(conv_frist_name, link)
print(articulo)


# def crear_archivo():
#         with open(str(pathlib.Path().absolute()) + "\\Archivo\\"+'Articulos.csv','a', newline='') as f:
#            # create the csv writer
#             writer = csv.writer(f)
#             #write a row to the csv file
#             writer.writerow(articulo)
