from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_sco_login():
    # open browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://192.168.6.24:6002/login")

    # enter username
    email_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//mat-label[normalize-space()='Email / Phone Number']/ancestor::mat-form-field//input"
        ))
    )
    email_field.send_keys("yahya.bin.naveed.jdl.com")

    # enter password
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//input[@placeholder='Enter your password']"
        ))
    )
    password_field.send_keys("Admin@123")

#checkbox
    remember_me = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Remember Me']"))
    )
    remember_me.click()

    # click Login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))
    )
    login_button.click()

    # optional: wait for dashboard or success element
    time.sleep(3)

    # check page title
    assert "SCO" in driver.title

    # close browser
    driver.quit()
