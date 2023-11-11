import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://platform.kodland.org/auth/")
time.sleep(5)

login = driver.find_element(By.NAME,"login")
password = driver.find_element(By.NAME,"password")
button = driver.find_element(By.TAG_NAME,"button")

login.send_keys("lgapiev")
time.sleep(1)
password.send_keys("nmz6e04Z8r")
time.sleep(1)
button.click()
time.sleep(1)

driver.get("https://platform.kodland.org/ru/task_57407/")
time.sleep(5)
for i in range(6):
    button_id = driver.find_element(By.ID,'sub-button')
    time.sleep(1)
    button_id.click()
    time.sleep(1)
    button_ok = driver.find_element(By.ID,'submit_task_button')
    time.sleep(1)
    button_ok.click()
    time.sleep(1)
    button_next = driver.find_element(By.ID,"next_task_button")
    time.sleep(1)
    button_next.click()
    time.sleep(1)
