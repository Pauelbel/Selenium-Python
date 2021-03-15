import math
from selenium import webdriver

# опция подавляющая ошибку Bluetooth 
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


browser = webdriver.Chrome(options=options, executable_path="C:\\Users\\pvbel\\Desktop\\QA-Engineer\\Selenium and Python automation\\drivers\\chromedriver.exe")
link = "http://suninjuly.github.io/math.html"
browser.get(link)

try:
    x_element = browser.find_element_by_id("input_value").text
    browser.find_element_by_id("answer").send_keys(calc(x_element))
    elements_to_select = tuple(("[id = 'robotCheckbox']", "[for=\"robotsRule\"]", "button.btn.btn-default"))
    print(x_element)
    for elem in elements_to_select:
        browser.find_element_by_css_selector(elem).click()

    print_answer(browser)
finally:
    browser.quit()