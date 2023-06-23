from selenium import webdriver
from twitterFile import TwitterClass
import json



driver=webdriver.Firefox()

accounts = [
    'https://twitter.com/salsichinhas',
    'https://twitter.com/TV5MONDE',
    'https://twitter.com/XM_COM'
]
# collection des  tweets de tous les comptes
for account in accounts:
    driver.get(account)
    driver.implicitly_wait(10)
    data=TwitterClass.Accounttwitter(TwitterClass,driver)
    json_data = json.dumps(data, indent=4)
    #enregistrement des données en formts JSON  
    with open('Accountsdata/'+data['User_name']+'.json', 'w') as file:
        file.write(json_data)
    print('JSON file saved.')
driver.quit()
