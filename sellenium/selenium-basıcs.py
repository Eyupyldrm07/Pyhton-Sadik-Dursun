from selenium import webdriver
import time 
driver = webdriver.Firefox()


url = 'https://github.com/'
driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot('githup.com-homepage.png')


url='https://github.com/Eyupyldrm07'

driver.get(url)

print(driver.title)

if 'Eyupyldrm07' in driver.title:
    driver.save_screenshot('githup-eyuplyildirim.png')

time.sleep(2)

driver.back()
# driver.forward()
time.sleep(2)


driver.close()