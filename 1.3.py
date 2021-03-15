# перебор лишних полей циклом (использование метода find_elements_by)
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
       element.send_keys("ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text

    alert.accept()
    print(alert_text.split()[-1])

finally:
    time.sleep(30)
    browser.quit()
