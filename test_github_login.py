from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_github_login():
    # open browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://github.com/login")

    # enter username and password
    driver.find_element(By.ID, "login_field").send_keys("amnahaider313")
    driver.find_element(By.ID, "password").send_keys("Fatima*5678")

    # click login
    driver.find_element(By.NAME, "commit").click()
    time.sleep(3)

    # check page title
    assert "GitHub" in driver.title
    #