import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    #ln(abs(12 * sin(x)))
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    value_element = browser.find_element(By.ID, 'input_value')
    value = value_element.text
    res = calc(value)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(res)

    submit = browser.find_element(By.TAG_NAME, 'button')
    submit.click()

finally:
    time.sleep(7)
    browser.quit()

