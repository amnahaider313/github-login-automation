from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup browser
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment if you want CI/CD mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 15)

try:
    # Step 1: Open app
    driver.get("http://192.168.6.24:6002/login")

    # Step 2: Login
    email = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//mat-label[normalize-space()='Email / Phone Number']/ancestor::mat-form-field//input"))
    )
    email.send_keys("yahya.bin.naveed@gmail.com")

    pwd = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']")))
    pwd.send_keys("Admin@123")

    remember = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Remember Me']")))
    remember.click()

    login = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']")))
    login.click()

    # Step 3: Wait for dashboard
    wait.until(EC.title_contains("SCO"))
    time.sleep(2)

    print("✅ Logged in successfully")

    # Step 4: Loop through all sidebar items dynamically
    xpath_pattern = "//span[@mattooltip]"  # adjust if sidebar locator differs
    sidebar_items = driver.find_elements(By.XPATH, xpath_pattern)
    total = len(sidebar_items)
    print(f"Found {total} menu items.")

    for i in range(total):
        # Re-fetch items each time (avoid stale element)
        items = driver.find_elements(By.XPATH, xpath_pattern)

        if i >= len(items):
            break

        tooltip = items[i].get_attribute("mattooltip")
        print(f"\n👉 Clicking menu {i+1}/{total}: {tooltip}")

        try:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", items[i])
            driver.execute_script("arguments[0].click();", items[i])
            time.sleep(2)

            print(f"✅ Opened: {tooltip} — {driver.current_url}")
        except Exception as e:
            print(f"❌ Failed to click '{tooltip}' - {e}")

finally:
    driver.quit()
