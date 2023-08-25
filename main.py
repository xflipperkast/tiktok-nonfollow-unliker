import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

# Ask how many times to check a video
num_checks = int(input("How many video's do you want to check? "))

# Specify the path for the profile directory named "ttaut"
profile_path = os.path.join(os.getcwd(), 'ttaut')

# Set up Chrome options with the profile path
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={profile_path}")

# Set up the Chrome Service
chrome_service = ChromeService(executable_path='chromedriver.exe')

# Set up the WebDriver with the Chrome Service and options
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigate to the login page (or any other actions you want to perform)
driver.get('https://www.tiktok.com/?lang=nl-NL')

# Wait for you to log in
input("Please log in on the opened browser window, then type 'yes' and press Enter here to continue... ")

for _ in range(num_checks):
    try:
        # Check if following the person
        follow_button = driver.find_element(By.CSS_SELECTOR, '.tiktok-1djnsui-ButtonLabel.e1v8cfre3')
        if 'Volgend' not in follow_button.text:
            print('Not following. Unliking video.')
            try:
                like_button = driver.find_element(By.CSS_SELECTOR, 'button.tiktok-1ei6d3j-ButtonActionItem.e1hk3hf90')
                like_button.click()
                print('Video is unliked.')
            except ElementClickInterceptedException:
                print("An element is blocking the like button. Please manually handle this situation.")
                input("Once you have handled the issue, type 'done' and press Enter here to continue... ")
                like_button.click()
        else:
            print('Following the person.')
    except NoSuchElementException:
        print("Follow button does not exist. Scrolling down...")

    # Scroll down by sending the "ARROW_DOWN" key
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_DOWN)

    # Wait for 5 seconds
    time.sleep(1)

# Close the browser
driver.quit()
