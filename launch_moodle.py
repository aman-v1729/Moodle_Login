from selenium import webdriver
import getpass

username = 'cs5190419'
password = getpass.getpass()

driver = webdriver.Chrome("chromedriver")
driver.get("https://moodle.iitd.ac.in/login/index.php")


def login(username, password):
    username_field = driver.find_element_by_id("username")
    password_field = driver.find_element_by_id("password")
    captcha_field = driver.find_element_by_id("valuepkg3")
    login_btn = driver.find_element_by_id("loginbtn")

    username_field.clear()
    password_field.clear()
    captcha_field.clear()

    captcha = driver.find_element_by_id("login").text
    fl = False
    for i in captcha.split():
        if(i.isnumeric() and not fl):
            num1 = int(i)
            fl = True
        elif(i.isnumeric()):
            num2 = int(i)
            break
    # print(num1, num2)

    if 'first' in captcha:
        sol = num1
    if 'second' in captcha:
        sol = num2
    if 'add' in captcha:
        sol = num1 + num2
    if 'subtract' in captcha:
        sol = num1 - num2

    username_field.send_keys(username)
    password_field.send_keys(password)
    captcha_field.send_keys(str(sol))

    login_btn.click()


login(username, password)

# driver.quit()
