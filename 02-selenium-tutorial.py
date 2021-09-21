# Page navigating and Clicking elements

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to chromedriver
PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)
URL = "https://techwithtim.net"

# driver opens URL
driver.get(URL)

link = driver.find_element_by_link_text("Python Programming")
# This allows us to type a text that shows up for a link and it accesses the element from that
link.click() # moves to the next page

try: # this will wait 10 seconds for the driver to find an element present on the page that has the LINK_TEXT of X
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()

    driver.back() # goes to the previous page
    driver.back()
    driver.back()
    driver.forward() # goes to the next page
    driver.forward()

except:
    driver.quit()
