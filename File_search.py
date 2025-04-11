from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time

file_path=input("Please type the file path of the image you want to search: ")
#I use this path to test: /Users/jiangnan/Study/FUN/projects_public/Mac-Google-Lens/rXe9Q.png
#or also this:/Users/jiangnan/Study/FUN/projects_public/Mac-Google-Lens/medicine.jpg
#so it works for different image types. 

options = webdriver.ChromeOptions() 
options.add_argument('user-data-dir=./chrome_profile')
# options.add_argument('profile-directory=Profile 1')
# /private/var/folders/mz/2nyzsnvd3n1_31l14sf13sf80000gn/T/.org.chromium.Chromium.qPqhxX/Default
# /private/var/folders/mz/2nyzsnvd3n1_31l14sf13sf80000gn/T/.org.chromium.Chromium.ET2FvZ/Default

#it can't run more than once when the chrome is opened.
driver = webdriver.Chrome(options=options)
driver.get("https://images.google.com/")
wait = WebDriverWait(driver,5)

# try:
#     wait.until(
#         lambda _: driver.find_element(By.XPATH, "//button/div[contains(text(), 'Accept all')]/..") 
#     )
#     driver.find_element(By.XPATH, "//button/div[contains(text(), 'Accept all')]/..").click()
# except:
#     pass

get_accept_all = lambda: driver.find_elements(By.XPATH, "//button/div[contains(text(), 'Accept all')]/..")
get_search_by_image = lambda: driver.find_elements(By.CSS_SELECTOR, "div[aria-label='Search by image']")

wait.until(lambda _: get_accept_all() or get_search_by_image())


get_search_by_image= lambda: driver.find_elements(By.CSS_SELECTOR,"div[aria-label='Search by image']")
wait.until(lambda _: get_search_by_image())
# get_search_by_image().click()
# ele=get_search_by_image()
# ele.click()
driver.find_element(By.CSS_SELECTOR,"div[aria-label='Search by image']").click()

get_input_file= lambda: driver.find_elements(By.CSS_SELECTOR,'input[type=file]')
wait.until(lambda _: get_input_file())

# driver.find_element(By.CSS_SELECTOR,'input[type=file]').send_keys("/Users/jiangnan/Study/FUN/projects_public/Mac-Google-Lens/rXe9Q.png")

driver.find_element(By.CSS_SELECTOR,'input[type=file]').send_keys(file_path)

while True:
    time.sleep(1)
    try:
        driver.get_window_rect()
        #to test whether the window is closed or not
    except Exception:
        driver.quit()
        #when the window is closed, the program will quit.
        break