from selenium import webdriver
import time
from cred import user,password

class Bot():
    def __init__(self):
        self.driver=webdriver.Chrome()

    def click(self,xmap):
        but=self.driver.find_element_by_xpath(xmap)
        but.click()

    def login(self):  
        self.driver.get("https://tinder.com/") 
        time.sleep(3)
        
        self.click('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div/div/button')
        time.sleep(3)
        
        main_window=self.driver.window_handles[0]
        login_window=self.driver.window_handles[1]
        self.driver.switch_to_window(login_window)

        email_blank=self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_blank.send_keys(user)
        self.click('//*[@id="identifierNext"]/div/button')
        time.sleep(1)
        
        password_blank=self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        password_blank.send_keys(password)
        self.click('//*[@id="passwordNext"]/div/button')
        time.sleep(5)
        
        self.driver.switch_to_window(main_window)
        self.click('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        self.click('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        self.click('//*[@id="content"]/div/div[2]/div/div/div[1]/button')

    def swipe_right(self):
        self.click('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')

    def swipe_left(self):
        self.click('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')

    def match(self):
        time.sleep(0.5)

    def auto(self):
        while True:
            time.sleep(1)
            try:
                self.swipe_right()
            except Exception:
                try:
                    self.click('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
                except Exception:
                    try:
                        self.click('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
                    except Exception:
                        self.match()

bot=Bot()
bot.login()
time.sleep(5)
bot.auto()

