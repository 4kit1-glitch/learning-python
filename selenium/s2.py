# keepin the browser open

from selenium import webdriver


my_driver = webdriver.Firefox()

my_driver.get("https://www.ssdt.cm/login")

input("press enter to exit")