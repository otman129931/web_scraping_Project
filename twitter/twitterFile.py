from datetime import datetime, timedelta
import pytz
from selenium.webdriver.common.by import By
class TwitterClass:
    #collection des donner de chaque tweet
    def Onetweet(tweet):
        datatweet={}
        imgs=[]
        text=tweet.text
        datatweet["text"]=text
        images=tweet.find_elements(By.TAG_NAME, 'img')
        for image in images:
            src=image.get_attribute("src")
            imgs.append(src)
        datatweet["images"]=imgs
        links=tweet.find_elements(By.TAG_NAME, 'a')
        hashtag=[]
        href=[]
        for link in links :
            linkk=link.get_attribute("href")
            if 'hashtag' in linkk:
                hashtag.append(linkk)
            else:
                href.append(linkk)
        datatweet["hashtag"]=hashtag
        datatweet["href"]=href
        date=tweet.find_element(By.TAG_NAME, 'time').get_attribute('datetime')
        datatweet["date"]=date
        reply=tweet.find_element(By.XPATH, ' //div[@data-testid="reply"]').text
        datatweet["reply"]=reply
        like=tweet.find_element(By.XPATH, ' //div[@data-testid="like"]').text
        datatweet["like"]=like
        retweet=tweet.find_element(By.XPATH, ' //div[@data-testid="retweet"]').text
        datatweet["retweet"]=retweet
        return datatweet 
    #verfication si le date est dans les derniers 7  jours 
    def date_is_within_last_seven_days(date_string):
        date = datetime.fromisoformat(date_string.replace("Z", "+00:00"))
        date = date.astimezone(pytz.utc)
        current_date = datetime.now(pytz.utc)
        delta = current_date - date
        if delta <= timedelta(days=7):
            return True
        else:
            return False
    # collection des donneés de chque compte
    def Accounttwitter(self, driver):
        AccountData={}
        User_name=driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/h2/div/div/div/div/span[1]/span/span[1]').text
        AccountData['User_name']=User_name
        follower_count = driver.find_element(By.CSS_SELECTOR, 'div.r-13awgt0:nth-child(5) > div:nth-child(2) > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)').text
        AccountData['follower_count']=follower_count
        isdatein7days=True
        datatweets=[]
        while isdatein7days :
            try :
                tweet=driver.find_element(By.XPATH, '//article[@data-testid="tweet"]')
                data=self.Onetweet(tweet)
                date=data['date']
                isdatein7days=self.date_is_within_last_seven_days(date)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                driver.implicitly_wait(10)
                datatweets.append(data)
            except:
                break
        AccountData['tweets']=datatweets
        return AccountData

