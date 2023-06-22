from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import json
class Voiture:

    def CreditMetuel(driver):
        data = {}

        name = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div/article/div/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div[1]/p/strong').text
        price = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div/article/div/div/div/form/div[1]/div[2]/div[1]/div[3]/div/div/p/span[1]').text
        unit = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div/article/div/div/div/form/div[1]/div[2]/div[1]/div[3]/div/div/p/span[2]').text
        infos = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div/article/div/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div[2]/p').text
        image = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div/article/div/div/div/form/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/img').get_attribute("src")

        data['name'] = name
        data['price'] = price+'  '+unit
        data['infos'] = infos
        data['image'] = image

        table_id = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div/article/div/div/div/form/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/table/tbody')
        rows = table_id.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
        caracts = {}
        for row in rows:
            # Get the columns (all the column 2)
            col1 = row.find_elements(By.TAG_NAME, "th")[0]
            col2 = row.find_elements(By.TAG_NAME, "td")[0]
            caracts[col1.text]=col2.text
        data['caracteristique'] = caracts
        A_credit = {}

        Acredit = driver.find_element(By.XPATH, '//*[@id="I0:C.S:O:D"]').text
        men = driver.find_element(By.XPATH, '//*[@id="I0:C.S:S:O2"]').text + 'EUR/mois'
        dure = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div/article/div/div/div/form/div[1]/div[2]/div[2]/ul/li[2]/div/div/div[1]/div[3]/div[1]/div/div[2]/p[2]/span').text

        A_credit['Mensualité'] = men
        A_credit['Duree'] = dure

        Montant_emp = driver.find_element(By.XPATH, '//*[@id="I0:C.S:S:O6"]').text + 'EUR'
        A_credit['Montant_emprunté'] = Montant_emp

        MantantT = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div/article/div/div/div/form/div[1]/div[2]/div[2]/ul/li[2]/div/div/div[1]/div[3]/div[8]/div[1]/span[2]').text
        A_credit['Montant_total'] = MantantT

        element = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div/article/div/div/div/form/div[1]/div[2]/div[2]/ul/li[2]/div/div/div[1]/div[3]/div[8]/div[1]/span[2]')
        element.click()

        dontF = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div/article/div/div/div/form/div[1]/div[2]/div[2]/ul/li[2]/div/div/div[1]/div[3]/div[8]/div[2]/ul/li[1]/div/span[2]').text
        dontI = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div/article/div/div/div/form/div[1]/div[2]/div[2]/ul/li[2]/div/div/div[1]/div[3]/div[8]/div[2]/ul/li[2]/div/span[2]').text
        tauxF = driver.find_element(By.XPATH, '//*[@id="I0:C.S:S:L1.O11"]').text

        A_credit['dont_frais'] = dontF
        A_credit['dont_intérêts'] = dontI
        A_credit['taux_débiteur_fixe'] = tauxF

        CoutT = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div/article/div/div/div/form/div[1]/div[2]/div[2]/ul/li[2]/div/div/div[1]/div[3]/div[9]/div[1]/span[2]').text
        A_credit['Cout_total'] = CoutT
        mantM = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div/article/div/div/div/form/div[1]/div[2]/div[2]/ul/li[2]/div/div/div[1]/div[3]/div[9]/div[2]/ul/li/div/span[2]').text
        A_credit['montant_mensuel']=mantM
        data['A_credit'] = A_credit
        
        LLD = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div/article/div/div/div/form/div[1]/div[2]/div[2]/ul/li[1]/div/div[1]/div[3]/div/div[2]/p[1]').text
        duree = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div/article/div/div/div/form/div[1]/div[2]/div[2]/ul/li[1]/div/div[1]/div[3]/div/div[2]/p[2]').text
        Assurance = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div/article/div/div/div/form/div[1]/div[2]/div[2]/ul/li[1]/div/div[1]/ul/li[1]/div/div[2]/p[2]').text
        entretien = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div/article/div/div/div/form/div[1]/div[2]/div[2]/ul/li[1]/div/div[1]/ul/li[2]/div/div[2]/p').text
        En_location = {}
        En_location['LLD'] = LLD
        En_location['Duree'] = duree
        En_location['Assurance_emprunteur '] = Assurance
        En_location['Entretien_inclus'] = entretien
        data['En_location'] = En_location
        if name==None:
            return None
        return data
    def AllVoiture(self,driver):
        data={}
        link = driver.find_element(By.CSS_SELECTOR,'#cookieLBmainbuttons > span:nth-child(1) > span:nth-child(1) > span:nth-child(1) > a:nth-child(1)')
        link.click()
        driver.implicitly_wait(10)
        # Find the parent element
        parent_element = driver.find_element(By.XPATH, '//*[@id="menu_espace_particulier"]/div/ul/li[3]')

        # Update the value of the aria-expanded attribute
        driver.execute_script("arguments[0].setAttribute('aria-expanded', 'true')", parent_element)

        # Scroll the parent element into view
        driver.execute_script("arguments[0].scrollIntoView(true);", parent_element)

        # Create ActionChains instance
        actions = ActionChains(driver)

        # Move mouse to parent element
        actions.move_to_element(parent_element)

        # Perform the click action on the target element
        credit_element = driver.find_element(By.XPATH, '//*[@id="menu_espace_particulier"]/div/ul/li[3]/div/div/ul[1]/li/div/ul/li[11]/a')
        actions.click(credit_element).perform()
        driver.implicitly_wait(10)
        # driver.get('https://www.creditmutuel.fr/fr/particuliers/emprunter.html')
        driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div/article/div[1]/ul/li[1]/h2/a').click()
        driver.implicitly_wait(10)
        car_block=driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div/article/section[1]/div/div[2]/div/div/form/div[1]/div[2]/div/div[1]/div[1]/div/ul')
        cars=car_block.find_elements(By.XPATH, './li')
        i=1
        for car in cars :
            try:
                driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/main/div/article/section[1]/div/div[2]/div/div/form/div[1]/div[2]/div/div[1]/div[1]/div/ul/li['+str(i)+']/div/div[1]' ).click()
                driver.implicitly_wait(10)
                voit=self.CreditMetuel(driver)
                if voit != None :
                    data[voit['name']]=voit
                    driver.execute_script("window.history.go(-1)")  
                    driver.implicitly_wait(10)
            except:
                print("div not found")
            i+=1
        json_data = json.dumps(data, indent=4)
        with open('Data/Allcars.json', 'w') as file:
            file.write(json_data)

        print('JSON file saved.')
        return data
    def carBpCaracteristiques(driver):
        caracteristiques={}
        caract=driver.find_element(By.CLASS_NAME, "caracteristiques")
        items=caract.find_elements(By.CLASS_NAME, "itemliste")
        for item in items:
            key=item.find_element(By.TAG_NAME, "label").text
            value=item.find_element(By.TAG_NAME, "span").text
            caracteristiques[key]=value
        return caracteristiques
    def carBPloc(driver):
        Location={}
        prix=driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/section/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/div').text
        Location['prix']=prix
        premierLo=driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/section/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/p[1]/span').text
        Location['Premier_loyer_majore']=premierLo
        Nombre_de_loyers=driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/section/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/p[2]/span').text
        Location['Nombre_de_loyers']=Nombre_de_loyers
        Nombre_de_km_an=driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/section/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/p[3]/span').text
        Location['Nombre_de_km_an']=Nombre_de_km_an
        infos=driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/section/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/span').text
        Location['infos']=infos
        return Location
    def carBP(self,driver):
        onecar ={}
        name=driver.find_element(By.XPATH, '/html/body/div[1]/section[2]/div[2]/div/h1').text
        onecar['name']=name
        image = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/section/div[2]/div/div/div[1]/div[1]/div[1]/img').get_attribute("src")
        onecar['image']=image
        caracteristiques=self.carBpCaracteristiques(driver)
        onecar['caracteristiques']=caracteristiques
        Location=self.carBPloc(driver)
        onecar['Location']=Location
        return onecar
   
    def AllcarsBP(self, driver):
        data={}
        i=1
        while True:
            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/section/div[2]/div/div[2]/div/div[2]/div[1]/section/div/nav/ul/li["+str(i)+"]").click()
                driver.implicitly_wait(10)
                cars=driver.find_elements(By.CLASS_NAME, "global-link")
                count=0
                for car in cars :
                    link=car.get_attribute("href")
                    driver.implicitly_wait(10)
                    driver2=webdriver.Firefox()
                    driver2.get(link)
                    driver2.implicitly_wait(10)
                    infocar=self.carBP(self,driver2)
                    driver2.quit()
                    data[infocar['name']]=infocar
                    count+=1
                    if count==5:
                        break
                break    
                i+=1
            except:
                break
        json_data = json.dumps(data, indent=4)
        with open('Data/AllBPcars.json', 'w') as file:
            file.write(json_data)

        print('JSON file saved.')
    
        return data
        
