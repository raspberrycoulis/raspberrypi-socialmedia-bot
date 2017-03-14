#!/usr/bin/python

import tweepy
import urllib2
import time
from config import (
    tw_webhook,
    tw_cons_key,
    tw_cons_sec,
    tw_accs_tok,
    tw_accs_sec,
    tw_style,
    tw_userid,
    tw_handle
)

# Tweepy API - do not change
auth = tweepy.OAuthHandler(tw_cons_key, tw_cons_sec)
auth.set_access_token(tw_accs_tok, tw_accs_sec)
api = tweepy.API(auth)
follows = api.get_user(tw_userid)

# The function that does the magic - checks your Twitter user for the number of followers then sends this data to Slack to notify you.

def postToSlack():
    fans = str(follows.followers_count)
    data = '{"attachments":[{"fallback":"'+tw_handle+' has '+fans+' followers.","pretext":"'+tw_handle+' has '+fans+' followers.","color":"'+tw_style+'","fields":[{"title":"Twitter Fans","value":"'+tw_handle+' has '+fans+' followers.","short":false}]}]}'
    slack = urllib2.Request(tw_webhook, data, {'Content-Type': 'application/json'})
    f = urllib2.urlopen(slack)
    f.close()

postToSlack()

exit()