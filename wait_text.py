import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    #ln(abs(12*sin(x)))
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button.click()

    browser.execute_script("window.scrollBy(0, 100);")

    value_element = browser.find_element(By.ID, "input_value")
    value = value_element.text
    res = calc(value)

    answer_element = browser.find_element(By.ID, "answer")
    answer_element.send_keys(res)

    submit = browser.find_element(By.ID, "solve")
    submit.click()


finally:
    time.sleep(5)
    browser.quit()

