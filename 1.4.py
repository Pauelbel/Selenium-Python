# перебор лишних полей циклом (поиск элемента по XPath)
from selenium import webdriver
import time
from lib2to3.pgen2 import driver


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
       element.send_keys("ответ")

    button = browser.find_element_by_xpath("/html/body/div[1]/form/div[6]/button[3]") # более не буду копировать пути из браузера
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text

    alert.accept()
    print(alert_text.split()[-1])

finally:
    time.sleep(10)
    browser.quit()
