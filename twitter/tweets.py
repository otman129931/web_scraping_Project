from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Spécifiez le chemin vers le driver Chrome WebDriver
#driver_path = '/chemin/vers/le/driver/chromedriver'

# Configurez les options du navigateur
#chrome_options = Options()
#chrome_options.add_argument("--headless")  # Exécuter en mode headless, sans ouvrir de fenêtre de navigateur

# Créez le service WebDriver
#service = Service(driver_path)

# Instanciez le navigateur Chrome WebDriver
driver=webdriver.Firefox()
#driver = webdriver.Chrome(service=service, options=chrome_options)

# Comptes Twitter à analyser
accounts = [
    'https://twitter.com/salsichinhas',
    'https://twitter.com/tousuncotefoot',
    'https://twitter.com/ActuFoot_'
]
driver.get('https://twitter.com/tousuncotefoot')
time.sleep(5)
follower_count = driver.find_element(By.CSS_SELECTOR, 'div.r-13awgt0:nth-child(5) > div:nth-child(2) > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)').text
print('Nombre de followers:', follower_count)
# tweets = driver.find_elements(By.CSS_SELECTOR, 'section.css-1dbjc4n > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
tweets = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="cellInnerDiv"]')
print(len(tweets))
# for tweet in tweets:
#         # Contenu du tweet
#         tweet_text = tweet.find_element(By.CSS_SELECTOR, 'div[data-testid="tweet"]').text
#         print('Contenu du tweet:', tweet_text)

#         # Métriques du tweet
#         likes_count = tweet.find_element(By.CSS_SELECTOR, 'div[data-testid="like"]').text
#         retweets_count = tweet.find_element(By.CSS_SELECTOR, 'div[data-testid="retweet"]').text
#         shares_count = tweet.find_element(By.CSS_SELECTOR, 'div[data-testid="reply"]').text
#         print('Nombre de likes:', likes_count)
#         print('Nombre de retweets:', retweets_count)
#         print('Nombre de partages:', shares_count)

# for account in accounts:
#    

#     # Récupération des tweets
#     tweets = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="tweet"]')
#     for tweet in tweets:
#         # Contenu du tweet
#         tweet_text = tweet.find_element(By.CSS_SELECTOR, 'div[data-testid="tweet"]').text
#         print('Contenu du tweet:', tweet_text)

#         # Métriques du tweet
#         likes_count = tweet.find_element(By.CSS_SELECTOR, 'div[data-testid="like"]').text
#         retweets_count = tweet.find_element(By.CSS_SELECTOR, 'div[data-testid="retweet"]').text
#         shares_count = tweet.find_element(By.CSS_SELECTOR, 'div[data-testid="reply"]').text
#         print('Nombre de likes:', likes_count)
#         print('Nombre de retweets:', retweets_count)
#         print('Nombre de partages:', shares_count)

#     print('---')

# Fermez le navigateur
# driver.quit()
