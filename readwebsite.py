from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 

# SEARCH = 'site: lever.co | site:greenhouse.io | site:workday.com software engineer | devops | data scientist | blockchain ("new grad" OR "1 year of experience" OR "2 year of experience")'
# SEARCH = "https://www.selenium.dev/selenium/web/web-form.html"

driver = webdriver.Chrome()

driver.get("http://iomersajid.pw")

# SEARCH = input("What do you want to search?")

# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys(SEARCH)
# search_box.send_keys(Keys.RETURN)

driver.implicitly_wait(2)

results = driver.find_elements(By.XPATH, "//img[@src='https://github.com/github.png']")
# print(type(results))
for result in results:
    print(result.get_attribute("src"))


driver.close()

# driver.close()