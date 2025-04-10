from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions() 
options.add_argument('user-data-dir=./chrome_profile')

driver = webdriver.Chrome(options=options)
driver.get("https://images.google.com/")
wait = WebDriverWait(driver,5)

get_accept_all = lambda: driver.find_elements(By.XPATH, "//button/div[contains(text(), 'Accept all')]/..")
get_search_by_image = lambda: driver.find_elements(By.CSS_SELECTOR, "div[aria-label='Search by image']")

wait.until(lambda _: get_accept_all() or get_search_by_image())

if get_accept_all():
    driver.find_element(By.XPATH, "//button/div[contains(text(), 'Accept all')]/..").click()

wait.until(lambda _: driver.find_element(By.CSS_SELECTOR, "div[aria-label='Search by image']"))
elem= driver.find_element(By.CSS_SELECTOR, "div[aria-label='Search by image']").click()

# wait.until(lambda _: driver.find_element(By.CSS_SELECTOR, "input[type=file]"))
# driver.find_element(By.CSS_SELECTOR, "input[type=file]").send_keys("/Users/jiangnan/Study/FUN/projects_ongoing/Mac-Google-Lens/rXe9Q.png")

wait.until(lambda _: driver.find_element(By.CSS_SELECTOR, "input.cB9M7"))
#also, I can use 'input[placeholder]' to find the element.
ele=driver.find_element(By.CSS_SELECTOR, "input[placeholder]")
actions=ActionChains(driver)
actions.move_to_element(ele).click(ele)
actions.key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()


import time

while True:
    time.sleep(1)
    try:
        driver.get_window_rect()
        #to test whether the window is closed or not
    except Exception:
        driver.quit()
        #when the window is closed, the program will quit.
        break