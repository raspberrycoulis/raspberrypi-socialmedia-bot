#!/usr/bin/python

import tweepy

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

# Displays the number of followers for the user in the terminal

#print(follows.followers_count)

# Experimenting with a function

def followers():
    look = follows.followers_count
    return (look)

followers()