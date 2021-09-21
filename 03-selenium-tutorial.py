# ActionChains and Automating Cookie Clicker

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Path to chromedriver
PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)
URL = "https://orteil.dashnet.org/cookieclicker/"
driver.get(URL) # driver opens URL

driver.implicitly_wait(5) # the line won't cast, only after 5 seconds

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range (1,-1,-1)]

actions = ActionChains(driver) # we can created a predefined list of actions that we want to preform in a specific sequence with ActionChains
actions.click(cookie)

for i in range (5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()





