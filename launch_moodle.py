from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass
import sys


def login(driver, username, password):
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

    print("Logging in as: cs5190419")
    login_btn.click()


def navigate(driver, course_code):
    FOUND = False
    curr_page = 0
    page_div = driver.find_element_by_id("pb-for-in-progress")
    total_pages = int(page_div.get_attribute("data-page-count"))
    while(curr_page < total_pages and not FOUND):
        curr_page += 1
        try:
            course_link = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located(
                    (By.PARTIAL_LINK_TEXT, course_code))
            )
            course_link.click()
            FOUND = True
            print("Found! Opening course page.")
        except:
            if(curr_page != total_pages):
                next_page = driver.find_element_by_link_text(str(curr_page+1))
                next_page.click()

    if(not FOUND):
        print("Error404: " + course_code + " Not Found!")
        if(total_pages > 1):
            driver.find_element_by_link_text('1').click()
            print("Redirecting back to page 1..")


if __name__ == '__main__':
    username = 'cs5190419'
    print(f'Username: {username}')
    password = getpass.getpass()
    course_code = False
    if(len(sys.argv) > 1):
        course_code = sys.argv[1].upper()
        # print(course_code)
        if(len(course_code) != 6 or not course_code[:3].isalpha() or not course_code[3:].isnumeric()):
            course_code = False
    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(options=options)
    driver.get("https://moodle.iitd.ac.in/login/index.php")

    login(driver, username, password)
    assert 'Dashboard' in driver.title
    print('Logged in successfully..')
    print('-------------------------')

    if(course_code):
        print('Searching for ' + course_code)
        navigate(driver, course_code)
    else:
        'Invalid Course Code Format!'
    # driver.quit()
