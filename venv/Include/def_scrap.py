import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from selenium import webdriver
import numbers
import pandas as pd
import time



site = "http://covid19dev.jatimprov.go.id/xweb/draxi"
#hdr = {'user-agent' : 'GoogleChrome'}
driver = webdriver.Chrome(r"D:\New folder\chrome driver\chromedriver.exe")

driver.get(site)
#driver.implicitly_wait(10)
#driver.find_element_by_xpath('//*[@id="popupmodal"]/div/div/div[2]/button').click()
#y = 500
#   driver.execute_script("window.scrollTo(0, "+str(y)+")")
 #   y += 350
  #  time.sleep(4)

list_kabupaten = []
list_dataRaw = []
list_data_pdp = []
list_data_odp = []


data_raw = driver.find_elements_by_class_name('m-0')
for data in data_raw :
    data_item = data.text
    list_dataRaw.append(data_item)

data_positif = driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]')
for positif in data_positif :
    data_item_positif = positif.text

data_pdp = driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]')
for pdp in data_pdp :
    data_item_pdp = pdp.text
    data_item_pdp2 = data_item_pdp.strip()
    numbers = [int(word) for word in data_item_pdp2.split() if word.isdigit()]
    list_data_pdp.append(numbers)

data_odp = driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[2]/div[3]')
for odp in data_odp :
    data_item_odp = odp.text





print(data_raw)
print(list_dataRaw)



print(data_item_positif)

print(data_item_odp)

print(list_data_pdp)
print('\t', data_item_pdp)
driver.quit()


"""
delay = 5 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/h6[1]')))
    print("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")
"""
