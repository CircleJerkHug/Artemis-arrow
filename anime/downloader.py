from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
driver.get("https://kissanime.ru/")
driver.maximize_window()



search = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "keyword"))).click()
search=driver.find_element_by_xpath('//*[@id="keyword"]')
search.send_keys("boruto")
search.send_keys(Keys.RETURN)
