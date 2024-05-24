from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(
)

url='https://github.com/'

driver.get(url)

searchInput = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div/div/qbsearch-input/div[1]/div/modal-dialog/div/div/div/form/query-builder/div[1]/div[1]/div/div[2]/input')
time.sleep(1)

searchInput.click()  # Öğeyi tıklayarak etkileşimli hale getirme
time.sleep(2)

searchInput.send_keys('python')
time.sleep(2)



# result = driver.page_source
# print(result)

# result = driver.find_elements(By.CSS_SELECTOR,'.body div h1')
# for element in result:
#     print(element.text)



