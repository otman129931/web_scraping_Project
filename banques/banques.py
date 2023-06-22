from selenium import webdriver
from voiture import Voiture
driver=webdriver.Firefox()
accounts = [
    'https://www.creditmutuel.fr/fr/particuliers/epargne/livret-de-developpement-durable.html',
    'https://banque-populaire.loa-automobile.fr/annonces'
]
driver.get(accounts[1])
driver.implicitly_wait(10)
data=Voiture.AllcarsBP(Voiture,driver)
print(data)
