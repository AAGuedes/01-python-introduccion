from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

# Una vez terminada la creación del test, comentar estas líneas
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# browser = webdriver.Chrome(options=options)

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get("https://githum.com")

link = browser.find_element(By.LINK_TEXT, "Sign in")
link.click()

user_input = browser.find_element(By.ID, "login_field")
pass_input = browser.find_element(By.ID, "password")

user_input.send_keys(os.environ.get("gh_user"))
pass_input.send_keys(os.environ.get("gh_pass"))
pass_input.send_keys(Keys.RETURN)

profile = browser.find_element(
    By.CLASS_NAME,
    "css-truncate.css-truncate-target.ml-1"
)
label = profile.get_attribute("innerHTML")

assert "JohnDoe" in label

browser.quit()
