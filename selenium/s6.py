# practice with iframes

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException


my_driver = webdriver.Firefox()
url = "https://the-internet.herokuapp.com/iframe"

try:
    my_driver.get(url)
    wait = WebDriverWait(my_driver, 10)

    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "mce_0_ifr"))) # switch when the page is ready

    text_box = my_driver.find_element(By.ID, "tinymce")
    text_box.clear()    # clears the text entry if possible

    text_box.send_keys("HELLO FROM KITS LAPTOP")

    # switch back to main content
    my_driver.switch_to.default_content()

    input("...")

except WebDriverException as err:
    print(f"some error occured: {err}")
finally:
    my_driver.quit()

