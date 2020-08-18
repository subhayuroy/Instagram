from selenium import webdriver
from time import sleep
from cryptography.fernet import Fernet

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log In')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath('//button[@ype= "submit"]').click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)

def get_unfollowers(self):
    self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username)).click()

key = Fernet.generate_key() #this is your "password"
cipher_suite = Fernet(key)
pw = input("Enter your Instagram password: ")
encoded_text = cipher_suite.encrypt(pw)
decoded_text = cipher_suite.decrypt(encoded_text)
my_bot = InstaBot('the_shadow_of_a_tear', decoded_text)
