from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")
    wait = WebDriverWait(driver, 15)

    # дождаться, пока будет можно кликнуть
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ajaxButton")))
    button.click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content")))
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR, "#content").text.strip() != "")

    print(driver.find_element(By.CSS_SELECTOR, "#content").text)

    # задержка на экране 5 сек
    start = time.time()
    WebDriverWait(driver, 5).until(lambda d: time.time() - start >= 2)

except TimeoutException:

    pass
finally:
    driver.quit()