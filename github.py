from usernameandpassword import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Github:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
    
    def logIn(self):
        self.browser.get("https://github.com/")
        self.browser.maximize_window()
        time.sleep(2)

        self.search_signIn = self.browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[2]/a")
        self.search_signIn.send_keys(Keys.ENTER)
        time.sleep(2)
    

        self.search_username = self.browser.find_element(By.XPATH, '//*[@id="login_field"]')
        self.search_username.send_keys(username)
        time.sleep(2)

        self.search_password = self.browser.find_element(By.XPATH, '//*[@id="password"]')
        self.search_password.send_keys(password)
        time.sleep(2)

        self.search_complete = self.browser.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[11]')
        self.search_complete.send_keys(Keys.ENTER)
        time.sleep(2)
    

    def EnterProfile(self):
        self.openProfile = self.browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div[7]/details/summary")
        self.openProfile.send_keys(Keys.ENTER)
        time.sleep(2)

        self.enterProfile = self.browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div[7]/details/details-menu/a[1]")
        self.enterProfile.send_keys(Keys.ENTER)
        time.sleep(5)
    
    def CaptureRepos(self):
        self.repoNames = []
        self.openRepo = self.browser.find_element(By.XPATH, "/html/body/div[1]/div[5]/main/div[1]/div/div/div[2]/div/nav/a[2]")
        self.openRepo.send_keys(Keys.ENTER)
        time.sleep(5)

        self.getRepoNames = self.browser.find_elements(By.ID, "user-repositories-list")


        for item in self.getRepoNames:
            self.repoNames.append(item.find_element(By.CLASS_NAME, "d-inline-block mb-1").text) 
        time.sleep(5)
        print(self.repoNames)





github = Github(username, password)
github.logIn()
github.EnterProfile()
# github.CaptureRepos()

github.browser.close()