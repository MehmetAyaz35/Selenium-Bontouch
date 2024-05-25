from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup driver, for example using Chrome
driver = webdriver.Chrome()

try:
    # Navigate to the website
    driver.get('https://www.bontouch.com/')

    # Close cookies alert if needed, make sure this element exists and is visible
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'cookie_action_close_header_reject'))).click()

    # Open the menu
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cm-header-wrapper > .menu-toggle-btn'))).click()

    # Navigate to careers by clicking the relevant menu item
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ':nth-child(9) > a > span'))).click()

    # Dismiss additional cookie settings if present
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-action="click->common--cookies--alert#disableAll"]'))).click()

    # Click on the specific career link
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="https://careers.bontouch.com/connect"]'))).click()

    # Click on a button inside a link to navigate further or confirm action
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="https://careers.bontouch.com/connect"] > .flex'))).click()

    # Click on a department button if needed to open a form or dropdown
    department_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-connect--signup-form-target="departments"] > .button')))
    department_button.click()
    department_button.click()  # clicking twice if necessary

    # Check checkboxes for consents
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'candidate_consent_given'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'candidate_consent_given_future_jobs'))).click()

    # Enter an email
    email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'candidate_email')))
    email_field.send_keys('mehmet.90.ayaz@gmail.com')

    # Simulate wait
    driver.implicitly_wait(1)

    # Click a potentially hidden element
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[class="absolute inset-0 flex items-center justify-center opacity-0 transition transition-opacity"]'))).click()

finally:
    # Close the driver
    driver.quit()



