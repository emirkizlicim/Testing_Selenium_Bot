from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()       #chrome kullan.

url = "https://github.com/"
driver.get(url)               #sayfayı ac.
driver.maximize_window()

serachInput = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]")     #location bulduruyoruz.
time.sleep(1)
serachInput.send_keys("python")                     #buldurğumuz location'a "python" gondriyor.
time.sleep(2)
serachInput.send_keys(Keys.ENTER)                 #keys imported. enter tuşunu atadık kendisi entera basıyor.
time.sleep(2)


# result = driver.find_elements(By.XPATH, "/html/body/div[1]/div[4]/main/div/div[3]/div/ul/li[1]/div[2]/div[1]/div[1]/a")

# for element in result:
#     print(element.text)

# result = BeautifulSoup(driver.page_source) 
# print(result.prettify())

time.sleep(5)
driver.close()
