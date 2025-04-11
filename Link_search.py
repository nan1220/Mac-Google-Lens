from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time

link=input("Please type the link of the image you want to search: ")
#I use this image link to test: pop cat
#https://images.steamusercontent.com/ugc/1654473538255844161/0EB3C8C0C310576DB910968D1F7C280FB3007D0B/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false

options = webdriver.ChromeOptions() 
options.add_argument('user-data-dir=./chrome_profile')

driver = webdriver.Chrome(options=options)
driver.get("https://images.google.com/")
wait = WebDriverWait(driver,5)

get_accept_all = lambda: driver.find_elements(By.XPATH, "//button/div[contains(text(), 'Accept all')]/..")
get_search_by_image = lambda: driver.find_elements(By.CSS_SELECTOR, "div[aria-label='Search by image']")

wait.until(lambda _: get_accept_all() or get_search_by_image())

wait.until(lambda _: driver.find_element(By.CSS_SELECTOR, "div[aria-label='Search by image']"))
elem= driver.find_element(By.CSS_SELECTOR, "div[aria-label='Search by image']").click()

wait.until(lambda _: driver.find_element(By.CSS_SELECTOR, "input.cB9M7"))
#also, I can use 'input[placeholder]' to find the element.

ele=driver.find_element(By.CSS_SELECTOR, "input[placeholder]")

ele.send_keys(link)
# ele.send_keys("https://images.steamusercontent.com/ugc/1654473538255844161/0EB3C8C0C310576DB910968D1F7C280FB3007D0B/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false")
ele.send_keys(Keys.RETURN) # press Enter




while True:
    time.sleep(1)
    try:
        driver.get_window_rect()
        #to test whether the window is closed or not
    except Exception:
        driver.quit()
        #when the window is closed, the program will quit.
        break