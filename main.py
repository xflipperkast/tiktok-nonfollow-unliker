import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from colorama import Fore, init

init()  # Initialize colorama

num_checks = int(input("How many video's do you want to check? "))
profile_path = os.path.join(os.getcwd(), 'ttaut')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={profile_path}")
chrome_service = webdriver.Chrome(service=webdriver.ChromeService(executable_path='chromedriver.exe'), options=chrome_options)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.get('https://www.google.com/')
print(Fore.GREEN + 'Go to TikTok via Google; otherwise, TikTok does not allow you to log in. XD')
input("Please log in on the opened browser window, then type 'yes' and press Enter here to continue... ")

following_texts = ['Following', 'Volgend', 'Folge ich', 'Seguindo', 'Siguiendo', 'Abonné']  # Additional languages
for _ in range(num_checks):
    try:
        follow_button = driver.find_element(By.CSS_SELECTOR, '.tiktok-1djnsui-ButtonLabel.e1v8cfre3')
        if not any(follow_text in follow_button.text for follow_text in following_texts):
            print(Fore.RED + 'Not following. Unliking video.')
            try:
                like_button = driver.find_element(By.CSS_SELECTOR, 'button.tiktok-1ei6d3j-ButtonActionItem.e1hk3hf90')
                like_button.click()
                print(Fore.GREEN + 'Video is unliked.')
            except ElementClickInterceptedException:
                print(Fore.RED + "A captcha is blocking the like button. Please manually handle this situation.")
                input("Once you have handled the issue, type 'done' and press Enter here to continue... ")
                like_button.click()
        else:
            print(Fore.GREEN + 'Following the person.')
    except NoSuchElementException:
        print(Fore.RED + "Follow button does not exist. Scrolling down...")
    
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_DOWN)
    time.sleep(1)

print(Fore.RESET)  # Resetting the color back to normal
driver.quit()
