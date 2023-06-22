from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time
driver=webdriver.Firefox()

accounts = [
    'https://www.creditmutuel.fr/fr/particuliers/epargne/livret-de-developpement-durable.html'
]
driver.get(accounts[0])
time.sleep(5)
link = driver.find_element(By.CSS_SELECTOR,'#cookieLBmainbuttons > span:nth-child(1) > span:nth-child(1) > span:nth-child(1) > a:nth-child(1)')
link.click()
time.sleep(10)
# element = driver.find_element(By.CSS_SELECTOR, 'a[data-page="135956"]')
# driver.execute_script("arguments[0].setAttribute('aria-expanded', 'true')", element)
driver.get('https://www.creditmutuel.fr/fr/particuliers/emprunter.html')
driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div/article/div[1]/ul/li[1]/h2/a').click()
time.sleep(5)
car_block=driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div/article/section[1]/div/div[2]/div/div/form/div[1]/div[2]/div/div[1]/div[1]/div/ul')
cars=car_block.find_elements(By.XPATH, "/html/body/div[2]/div[3]/main/div/article/section[1]/div/div[2]/div/div/form/div[1]/div[2]/div/div[1]/div[1]/div/ul/li")
i=1
for car in cars :
    try:
         car.find_element(By.XPATH,'/html/body/div[2]/div[3]/main/div/article/section[1]/div/div[2]/div/div/form/div[1]/div[2]/div/div[1]/div[1]/div/ul/li['+str(i)+']/div/div[1]' ).click()
         print("imaeg clicked"+str(i))
    except:
         print("div not found")
    i+=1

