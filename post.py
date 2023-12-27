from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

current_directory = os.getcwd()
user_data_directory = os.path.join(current_directory, 'facebook', 'profile1')
# Set up Chrome options
option = webdriver.ChromeOptions()
option.add_argument(f'user-data-dir={user_data_directory}')
option.add_argument('--mute-audio')
option.add_experimental_option('excludeSwitches', ['enable-logging'])

# Create Chrome WebDriver
browser = webdriver.Chrome(options=option)
browser.set_window_size(800, 1200)

# Open Facebook group
browser.get("https://www.facebook.com/groups/539140943914264")
sleep(3)

post = browser.find_element(By.XPATH, '//*[@class="x1lliihq x6ikm8r x10wlt62 x1n2onr6"]')
post.click()
sleep(3)

input_field = browser.find_element(By.XPATH, '//*[@class="_1mf _1mj"]')
sleep(3)

file_path = 'content.txt'  
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

lines = content.splitlines()

for line in lines:
    input_field.send_keys(line.strip())
    input_field.send_keys(Keys.RETURN)
    sleep(1)

sleep(100)

# Close the browser
browser.quit()