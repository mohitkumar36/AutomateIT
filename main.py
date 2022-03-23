from selenium import webdriver
import os
import time
import getpass

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

credUser = input("Enter your Username: ")
credPass = getpass.getpass("Enter your Password: ")
user = input("Enter usernames of person you want to send texts: ").split()
message_ = input("Enter the text you want to send: ")
  
driver = webdriver.Chrome(ChromeDriverManager().install())

  
class bot:
    def __init__(self, username, password, user, message):
        self.username = username
        self.password = password
        self.user = user
        self.message = message
        self.base_url = 'https://www.instagram.com/'
        self.bot = driver
        self.login()
  
    def login(self):
        self.bot.get(self.base_url)
  
        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)
  
        # first pop-up
        self.bot.find_element(by = By.XPATH, value = '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(5)

        # 2nd pop-up
        self.bot.find_element(by = By.XPATH, value = '/html/body/div[6]/div/div/div/div[3]/button[2]').click()
        time.sleep(10)

  
        # direct button
        self.bot.find_element(by = By.XPATH, value = '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        time.sleep(4)
  
        

        for i in self.user:
            # clicks on pencil icon
            self.bot.find_element(by = By.XPATH, value = '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button/div').click()
            time.sleep(4)
  
            # enter the username
            self.bot.find_element(by = By.XPATH, value = '/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i)
            time.sleep(4)
  
            # click on the username
            self.bot.find_element(by = By.XPATH, value = '/html/body/div[6]/div/div/div[2]/div[2]/div[1]/div').click()
            time.sleep(4)
  
            # next button
            self.bot.find_element(by = By.XPATH, value = '/html/body/div[6]/div/div/div[1]/div/div[3]/div/button/div').click()
            time.sleep(4)
  
            # click on message area
            send = self.bot.find_element(by = By.XPATH, value = '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
  
            # types message
            send.send_keys(self.message)
            time.sleep(1)
  
            # send message
            send.send_keys(Keys.RETURN)
            time.sleep(2)
  
            # clicks on direct option or pencl icon
            self.bot.find_element(by = By.XPATH, value = '//*[@id="react-root"]/section/div/div[1]/div/div[3]/div/div[2]/a').click()
            time.sleep(4)

def init():
    bot(credUser, credPass, user, message_)
  
    # when our program ends it will show "done".
    print("DONE")


# calling the function
init()