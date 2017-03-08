#!/usr/bin/python

import tweepy
import urllib2
import time

# The time (in seconds) between checks. Default is 1800 seconds (30 minutes)
wait = 1800

# Replace with your incoming webhook URL generated in Slack
webhook = ''

# Colour for "OK" message
ok = "#74a727"

# Colour for "Uh oh!" message
warn = "#971a1a"

# Add the relevant keys, tokens and secrets from your Twitter app made here: https://apps.twitter.com/

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Define the user you want to track the followers of below (without the @)
user = 'raspberrycoulis'

# Tweepy API variables and stuff
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Defines the api variable for convenience

api = tweepy.API(auth)

# Tells the Tweepy API to get the user details specified earlier

follows = api.get_user(user)

# Experimenting with a function

def followers():
  while True:
    look = str(follows.followers_count)
    data = '{"attachments":[{"fallback":"'+user+' has '+look+' followers.","pretext":"'+user+' has '+look+' followers.","color":"'+ok+'","fields":[{"title":"OK","value":"'+user+' has '+look+' followers.","short":false}]}]}'
    slack = urllib2.Request(webhook, data, {'Content-Type': 'application/json'})
    f = urllib2.urlopen(slack)
    f.close()
    time.sleep(wait)

followers()