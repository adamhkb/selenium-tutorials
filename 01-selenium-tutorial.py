# Selenium Tutorial #1
# https://sites.google.com/a/chromium.org/chromedriver/downloads

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
print(driver.title)

search = driver.find_element_by_name("s") # Returns an object that represents that search bar that we can now interact with
search.send_keys("test") # searches the string 'test'
search.send_keys(Keys.RETURN) # press enter to start search

# print(driver.page_source) # prints entire source code of the page

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    ) # waits 10 seconds until it locates 'main' in the element html

    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text) # prints article summaries

finally:
    driver.quit()

# time.sleep(5) # delays the program by 5 seconds before quitting

