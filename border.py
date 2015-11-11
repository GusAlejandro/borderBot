import requests
import tweepy
from bs4 import BeautifulSoup
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)



class WaitTime:
    def __init__(self, url):
        self.url = url

#scrapes the indicated url and retrieves raw html    
    def webScrape(self):
        r = requests.get(self.url)
        data = r.text
        soup = BeautifulSoup(data,"html5lib")
        links = soup.find_all('td',class_="td_col_2")
        rawScrape = str((links[0]))
        return rawScrape

#parses html to extract the wait time as a string
    def getTime(self):
        rawS = self.webScrape()
        begin = rawS.index('<span')
        end = rawS.index('</span>')
        newString = rawS[begin:end]
        begin2 = newString.index('>')
        finalString = newString[begin2:]
        finalString = finalString[1:]
        return finalString

#creates all the objects needed with their corresponding url 
carSentri = WaitTime("http://traffic.calit2.net/border/border-wait-times.php?type=passenger&sub=nexus&port=250401")
carReady = WaitTime("http://traffic.calit2.net/border/border-wait-times.php?type=passenger&sub=ready&port=250401")
carReg = WaitTime("http://traffic.calit2.net/border/border-wait-times.php?type=passenger&sub=standard&port=250401")

walkReady = WaitTime("http://traffic.calit2.net/border/border-wait-times.php?type=pedestrian&sub=ready&port=250401")
walkReg = WaitTime("http://traffic.calit2.net/border/border-wait-times.php?type=pedestrian&sub=standard&port=250401")


def respondTweet():
    m = " VIA CAR: Sentri " + carSentri.getTime() + ", Ready Lane " + carReady.getTime() + ", Regular " + carReg.getTime() + " || ON FOOT: Ready Lane " + walkReady.getTime() + ", Regular " + walkReg.getTime() 
    api.update_status(status=m) 

respondTweet()
    
        
    





    
            
        
        