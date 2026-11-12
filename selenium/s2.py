# keepin the browser open

from selenium import webdriver


#my_driver = webdriver.Firefox()

#my_driver.get("https://www.ssdt.cm/login")

#input("press enter to exit")
#my_driver.quit()

## the selenium way better


# 1. Set up options to keep the browser open after the script finishes
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# 2. Launch the browser with these options
browser = webdriver.Firefox(options=options)

# 3. Go to a page
browser.get("https://www.inventwithpython.com")

# The script ends here, but the browser will stay open because of "detach"