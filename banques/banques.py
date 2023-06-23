from selenium import webdriver
from voiture import Voiture
import json
driver=webdriver.Firefox()
accounts = [
    'https://www.creditmutuel.fr/fr/particuliers/epargne/livret-de-developpement-durable.html',
    'https://banque-populaire.loa-automobile.fr/annonces'
]
#collection des données des deux sites 
dataCars={}
for account in accounts :
    if 'creditmutuel' in account:
        driver.get(account)
        datamutel=Voiture.AllCreditCras(Voiture,driver)
    elif 'populaire' in account:
        driver.get(account)
        dataBP=Voiture.AllcarsBP(Voiture,driver)
dataCars['creditmutuel']=datamutel
dataCars['banque_populaire']=dataBP
#enregistrement des données en formts JSON  
json_data = json.dumps(dataCars, indent=4)
with open('Data/Allcars.json', 'w') as file:
    file.write(json_data)
print('JSON file saved.')
