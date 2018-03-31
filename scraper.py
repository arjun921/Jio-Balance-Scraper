from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from bs4 import BeautifulSoup
import urllib.request


# server = "http://127.0.0.1:5000"

delay = 1
temp = "empty"
def selectEmailLogin(browser):
    print("selectEmailLogin")
    try:
        LoginWithEmail = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'pt1:r1:0:sb11:gl1')))
        if LoginWithEmail:
            LoginWithEmail.click()
            selectAndFill(browser)
            doLogin(browser)
    except TimeoutException:
        print(".", end=" ")
        selectEmailLogin(browser)

def selectUserName(browser):
    print("selectUserName")
    try:
        username = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'pt1:r1:1:sb11:it1::content')))
        return username
    except TimeoutException:
        print(".", end=" ")
        selectUserName(browser)


def selectPassword(browser):
    print("selectPassword")
    try:
        password = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'pt1:r1:1:sb11:it2::content')))
    except TimeoutException:
        selectPassword(browser)
    return password

def selectRememberMe(browser):
    print("selectRememberMe")
    try:
        rememberMe = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'pt1:r1:1:sb11:sbc1')))
    except TimeoutException:
        selectRememberMe(browser)
    return rememberMe

def selectAndFill(browser):
    print("selectAndFill")
    username = selectUserName(browser)
    password = selectPassword(browser)
    rememberMe = selectRememberMe(browser)
    rememberMe.click()
    username.send_keys("yourname@example.com")
    password.send_keys("YOURPASSWORD")

def doLogin(browser):
    print("logging in..")
    loginButton = browser.find_element_by_id('pt1:r1:1:sb11:cb1')
    loginButton.click()


def dataLeft():
    browser = webdriver.Chrome('chromeDrivers/chromedriver_mac') # pass path to specific webdriver executable.
    # download webdriver from https://sites.google.com/a/chromium.org/chromedriver/downloads
    # alternative browser drivers for firefox, safari etc are also available from their respective sites
    # phantomjs can be obtained from http://phantomjs.org
    # browser = webdriver.PhantomJS()
    # browser = webdriver.Safari()
    browser.get("https://www.jio.com/Jio/portal/jioLogin")
    selectEmailLogin(browser)
    time.sleep(10)
    delay = 2
    try:
        data = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID,'pt1:r1:0:r2:1:lstData:0:pgl3')))
        a = data
        soup = BeautifulSoup(a.get_attribute('innerHTML'), 'html.parser')
        x = soup.find_all('span',class_="leftValueText")
        browser.close()
        return x[0].contents[0]
    except Exception as inst:
        print (type(inst))
        dataLeft()


dataValue = dataLeft()
print(dataValue)
print("all done")
