#!/usr/bin/python

import tweepy
import urllib2
import time

# For Twitter: Add the relevant keys, tokens and secrets from your Twitter app made here: https://apps.twitter.com/

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Variables - configure the bits below to get your script working. 

wait = 12600        # Time (in seconds) between checks. Default is 12600 seconds (210 minutes / 3.5 hours).
style = "#1da1f2"   # Colour for the message - default is Twitter Bird blue
userid = ''           # The Twitter user you want to track the followers of (without the @)
handle = ''         # Tweak this to display the userid in a nicer format - i.e. "Raspberry Coulis" instead of "raspberrycoulis"

# Slack incoming webhook URL

webhook = ''

# Tweepy API - do not change
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
follows = api.get_user(userid)

# The function that does the magic - checks your Twitter user for the number of followers then sends this data to Slack to notify you.

def postToSlack():
#  while True:
    fans = str(follows.followers_count)
    data = '{"attachments":[{"fallback":"'+handle+' has '+fans+' followers.","pretext":"'+handle+' has '+fans+' followers.","color":"'+style+'","fields":[{"title":"Twitter Fans","value":"'+handle+' has '+fans+' followers.","short":false}]}]}'
    slack = urllib2.Request(webhook, data, {'Content-Type': 'application/json'})
    f = urllib2.urlopen(slack)
    f.close()
#    time.sleep(wait)

postToSlack()

exit()