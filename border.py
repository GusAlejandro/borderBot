import requests
from bs4 import BeautifulSoup
import tweepy 
import _json
import json 
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#everything above is just configs and imports

#both functions below are for editing the string to just be the wait time
def splitted(ztring):
    begin = ztring.index('<span')
    end = ztring.index('</span>')
    newString = ztring[begin:end]
    return newString

def reSplit(fString):
    begin = fString.index('>')
    newString = fString[begin:]
    newString = newString[1:]
    return newString

# Web Scrapes the wait time as raw string 
def getWait(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data,"html5lib")
    links = soup.find_all('td',class_="td_col_2 midx")
    newS = str((links[0])) 
    return newS

#gets wait time as string 
def carSentri():
    site = "http://traffic.calit2.net/border/border-wait-times.php?type=passenger&sub=nexus&port=250401"
    scrape = getWait(site)
    time = reSplit(splitted(scrape))
    return time

def carReady():
    site = "http://traffic.calit2.net/border/border-wait-times.php?type=passenger&sub=ready&port=250401"
    scrape =  getWait(site)
    time = reSplit(splitted(scrape))
    return time
    
def carReg():
    site = "http://traffic.calit2.net/border/border-wait-times.php?type=passenger&sub=standard&port=250401"
    scrape = getWait(site)
    time = reSplit(splitted(scrape))
    return time

def walkReady():
    site = "http://traffic.calit2.net/border/border-wait-times.php?type=pedestrian&sub=ready&port=250401"
    scrape = getWait(site)
    time = reSplit(splitted(scrape))
    return time
    
def walkReg():
    site = "http://traffic.calit2.net/border/border-wait-times.php?type=pedestrian&sub=standard&port=250401"
    scrape = getWait(site)
    time = reSplit(splitted(scrape))
    return time

#Re-write functions above so it is just one function and a series of variables where the URL's will be stored  

def respondTweet():
    m = " VIA CAR: Sentri " + carSentri() + ", Ready Lane " + carReady() + ", Regular " + carReg() + " || ON FOOT: Ready Lane " + walkReady()+ ", Regular " + walkReg() 
    api.update_status(status=m)
    

respondTweet()
