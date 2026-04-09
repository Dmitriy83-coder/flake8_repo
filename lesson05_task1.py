from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Открываем Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/classattr")

# Кликаем синий баттон
button = driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
button.click()

driver.switch_to.alert.accept()

driver.quit()