from selenium.webdriver.firefox.options import Options
from emailer import send_email_alert
from typing import Dict
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("--headless")
browser = webdriver.Firefox(firefox_options=options)

browser.get(
    'https://www.ikea.com/ca/en/p/sektion-base-cabinet-frame-white-30265386/')
item_name = "Sketion 30x base cabinets"


# ikea local storage thas the location information. It has an expirey date to...
delay = 5  # seconds

try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located(
        (By.CLASS_NAME, 'range-revamp-stockcheck__available-for-delivery-link')))
    browser.execute_script('document.body.style.MozTransform = "scale(0.3)";')
    browser.execute_script('document.body.style.MozTransformOrigin = "0 0";')
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")


assert 'IKEA' in browser.title


# elem = browser.find_element_by_link_text('Check in-store stock')
elem = browser.find_element_by_class_name(
    'range-revamp-stockcheck__available-for-delivery-link')
elem.click()
print("Done First Step")
WebDriverWait(browser, 1)


# Find store.
retryCount = 5
elem2 = None

WebDriverWait(browser, delay).until(EC.presence_of_element_located(
    (By.XPATH, "//div[@class='range-revamp-change-store__store']")))

elem2 = browser.find_elements_by_xpath(
        "//div[@class='range-revamp-change-store__store']")

print("Done Second Step")
if(len(elem2) == 0):
    print("ERROR: COULD NOT FIND ITEM")


# Check if item is in stock
for item in elem2:
    if("Burlington" in item.text):
        send_email_alert(item_name, ""+item.text)
        print("--== Item has stock: ")
        print(item.text)
        print(('In stock' in item.text))
        print(" ")

print("-Ending-")
browser.quit()
