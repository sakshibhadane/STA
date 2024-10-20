import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# GitHub credentials
username = "sakshibhadane"
password = "Sakshi_01"

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Head to GitHub login page
driver.get("https://github.com/login")

# Find username/email field and send the username itself to the input field
driver.find_element("id", "login_field").send_keys(username)

# Find password input field and insert password as well
driver.find_element("id", "password").send_keys(password)

# Click login button
driver.find_element("name", "commit").click()

WebDriverWait(driver, timeout=30)
# Wait for the ready state to be complete
WebDriverWait(driver, timeout=30).until(
    lambda x: x.execute_script("return document.readyState == 'complete'")
)

error_message = "Incorrect username or password."
# Get the errors (if there are)
errors = driver.find_elements("css selector", ".flash-error")

# If we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("[-] Login failed")
else:
    print("[+] Login successful")

# Close the driver
driver.close()
