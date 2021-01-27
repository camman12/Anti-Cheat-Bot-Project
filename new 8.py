from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox()


print("enter search term")
cheat = input()
driver.get("https://www.google.com/")
f = open("demofile2.txt", "a")
cam = driver.find_element_by_name("q")
cam.send_keys(cheat)
cam.send_keys(Keys.ENTER)

for x in range(1,8):
    time.sleep(3)
    xpath_ = '//*[@id="rso"]/div[' + str(x) + ']/div/div[1]/a'
    driver.find_element_by_xpath(xpath_).click()
    html_source = driver.page_source
    if "chegg" in driver.current_url:
        print("chegg will be implemented later")
        driver.back()
    elif cheat in html_source:
        print("SITE THAT CONTAINS CLASS MATERIALS:" + driver.current_url)
        f.write(driver.current_url + '\n')
        driver.back()
    
f.close()



#print(html_source)
