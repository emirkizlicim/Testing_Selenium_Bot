from selenium import webdriver
import time
driver = webdriver.Chrome()

url = "https://github.com"
driver.get(url)
time.sleep(2)
driver.maximize_window()

print("taking screenshot.")
driver.save_screenshot("github_auto_save.png")
time.sleep(2)

url_2 = "https://www.youtube.com/channel/UCx3HFHIjOUeCpaYrlYdFp4A"
driver.get(url_2)
time.sleep(2)

driver.save_screenshot("youtube_channel.png")

time.sleep(2)
driver.back()                      #bi sayfa oncesine geliyor. bi sonrası için  => (variable-name).forward()

print(driver.title)
time.sleep(2)

driver.close()
