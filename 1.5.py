# Уникальность селекторов
from selenium import webdriver
import time

# опция подавляющая ошибку Bluetooth 
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# !!!!Важно!!!! executable_path="" - путь к драйверу
try:
    link = ("http://suninjuly.github.io/registration2.html")
    browser = webdriver.Chrome(options=options, executable_path="C:\\Users\\pvbel\\Desktop\\QA-Engineer\\Selenium and Python automation\\drivers\\chromedriver.exe")
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath("/html/body[@class='bg-light']/div[@class='container']/form/div[@class='first_block']/div[@class='form-group first_class']/input[@class='form-control first']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("/html/body[@class='bg-light']/div[@class='container']/form/div[@class='first_block']/div[@class='form-group second_class']/input[@class='form-control second']")
    input2.send_keys("Ivan@gmail.com")
    input3 = browser.find_element_by_xpath("/html/body[@class='bg-light']/div[@class='container']/form/div[@class='first_block']/div[@class='form-group third_class']/input[@class='form-control third']")
    input3.send_keys("+79151111111")
    input4 = browser.find_element_by_xpath("/html/body[@class='bg-light']/div[@class='container']/form/div[@class='second_block']/div[@class='form-group second_class']/input[@class='form-control second']")
    input4.send_keys("Krasnodar")
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
