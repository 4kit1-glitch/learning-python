# practicing with selenium

import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC

url = "https://the-internet.herokuapp.com/login"

# catching web driver errors at top level since it's an external error
try:
    my_driver = webdriver.Firefox() # create dirver obj
except WebDriverException as e:
    print(f"err: {e}")
    sys.exit(1)


try:
    my_driver.get(url)

    # find the username element
    user_box = my_driver.find_element(By.ID, "username")

    user_box.send_keys("tomsmith")

    # find passcode element
    pass_box = my_driver.find_element(By.ID, "password")
    pass_box.send_keys("SuperSecretPassword!")


    # find botton and simulate click
    submit_bt = my_driver.find_element(By.CSS_SELECTOR, "button[type=submit]")

    submit_bt.click()

    success_banner = WebDriverWait(my_driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "flash.success"))
    )
    print("Login successful:", success_banner.text)

    # comfirm login by checking for  <div data-alert id='flash' class='flash success'>You logged into a secure area!

    success_banner = my_driver.find_element(By.CSS_SELECTOR, "div.flash.success")

    input("Press enter to continue")

except WebDriverException as e:
    print(f"error occured \nDetails: {e}")
    my_driver.quit()

