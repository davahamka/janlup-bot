import tweepy
import random
import time
  
consumer_key = "t9g5K0cJ34ATxPVuaQYdT2ETh"
consumer_secret_key = "ZyOJ2bTf2ENWfNfBFBoMwARsDnC3y75GhmXtn0DyC7LdpVtAxa"
acces_token = "1273650391993839618-YZfqafXdMWLqNPMV1cgwpVno0nCF8K"
acces_token_secret = "Wp03KNHYesU2w5gbvo1vmc5xXipDDFFsjLEjHEXEpnm31"



def main():
    bot = authenticate()
    while True:
        try:            
            kt = pilihKata()
            bot.update_status(kt.upper())
            print("bot selesai mentweet "+kt)
            time.sleep(2)
        except tweepy.TweepError:
            continue

def authenticate():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(acces_token, acces_token_secret)
    api = tweepy.API(auth)
    return api

def delayKak(a):
    time.sleep(a)

def pilihKata():
    file = open("katarandom.txt")
    content = file.read()
    file.close()
    katakata = content.split(",")
    kata = random.choice(katakata)
    return kata 

main()