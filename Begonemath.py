

import pyperclip as pc #copy/paste to clipboard
import os #pathing
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait #downloading and clicking
import time #slow down time
import re #search through strings


#relative file paths
userprofile = os.environ['USERPROFILE']
driverpath = os.path.join(userprofile, 'Documents', 'GitHub', 'ExtraCodingThings', 'chromedriver_win32', 'chromedriver.exe')
print(driverpath)
url = "https://www.4devs.com.br/gerador_de_cpf"

def open_browser():
    """
    driver = webdriver.Chrome(driverpath)
    driver.get("https://www.codesters.com/code/")
    driver.find_element_by_id('top-nav-login-button').click()
    driver.get("https://www.codesters.com/login/clever/?next=/social-signup/")
    clever_ref_url = driver.current_url
    m = re.match('redirect_uri=(.*?)', "ref").group()
    print(clever_ref_url)
    #re.match("(.*?):",string).group()
    if m:
        found = m.group(1)
    print(m)
    print(found)
    time.sleep(5)
    driver.get("https://clever.com/oauth/authorize?state=vjqCqVqqEpUkC6QYauqVBdwfg4a607j0&redirect_uri=")
    time.sleep(30)
    """
    driver = webdriver.Chrome(driverpath)
    time.sleep(3)
    print(url)
    driver.get(url)
    driver.find_element_by_id('bt_gerar_cpf').click()
    text_field = driver.find_element_by_id('texto_cpf')
    text = wait(driver, 10).until(lambda driver: not text_field.text == 'Gerando...' and text_field.text)
    return text

#open_browser()

print(open_browser())


#logic in the code
one = 10
two = 8
three = 4



#logic in the thing

math = 2 ** 3 // 4 + 3
print(math)
pc.copy(math)
#text2 = pc.paste()


x = 2
y = 3
z = x ** y
print(z)