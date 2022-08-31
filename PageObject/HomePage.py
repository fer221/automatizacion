from selenium.webdriver.common.by import By

base_url = "https://www.mercadolibre.cl/"

class HomePage:
    def __init__(self, driver):
        self.driver = driver
    ingreso = (By.ID,"cb1-edit") 
    click = (By.XPATH, "//button[@class='nav-search-btn']")
    div_tshirt = (By.XPATH, "//div[@class='ui-search-result__content-wrapper']")
 
    


   
    