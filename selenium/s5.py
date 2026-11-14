# practicing with explicit waits 
# simulates a 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://the-internet.herokuapp.com/dynamic_loading/2"


my_driver = webdriver.Firefox()
my_driver.get(url)

start_bt = my_driver.find_element(By.CSS_SELECTOR, "div#start button")

start_bt.click()

wait = WebDriverWait(my_driver, 10)

wait.until(EC.visibility_of_element_located((By.ID, "finish")))

finish_elem = my_driver.find_element(By.CSS_SELECTOR, "div#finish h4")


print(finish_elem.text)
input("...")

my_driver.quit()
