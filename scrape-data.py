import tweepy
import codecs
import my_keys
import sys

# This makes strange characters work with Windows--comment out line 7 for Macs
sys.stdout.reconfigure(encoding='utf-8')
# Fair warning -- this only works with Python 3.7 or higher on Windows, and even then, it may still return errors for some computers.
# Get the authentication keys from my_keys.py
CONSUMER_KEY = my_keys.CONSUMER_KEY
CONSUMER_SECRET = my_keys.CONSUMER_SECRET
ACCESS_KEY = my_keys.ACCESS_KEY
ACCESS_SECRET = my_keys.ACCESS_SECRET

# Authenticate to Twitter with our keys
auth1 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth1.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth1)

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        tweet = status.text
        user = status.author
        userid = status.author.id
        time = status.created_at
        source = status.source
        tweetid = status.id

        if not ('RT @' in tweet) :	
            print("\"%s\",\"%s\",\"%s\",\"%s\",\"%s\"" % (tweet,user,userid,time,source))

StreamListener = StreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=StreamListener)
            
myStream.filter(track=['python'])
