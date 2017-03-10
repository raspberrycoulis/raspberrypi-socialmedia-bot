#!/usr/bin/python

import urllib2
from urllib import quote
import json

# Variables - configure the bits below to get your script working. 

style = '#3b5998'   # Colour for the message - default is Facebook blue
fb_page = ''        # Facebook Page name

# Slack incoming webhook URL

webhook = ''

# The functions that creates the magic - checks your Facebook Company Page for the number of fans then sends this data to Slack to notify you.

def fanCount():
    fb_id, access_key, secret = '', '', ''
    fb_url = 'https://graph.facebook.com/{}?access_token={}|{}&fields=fan_count'.format(quote(fb_id), quote(access_key), quote(secret))
    fanCount = urllib2.urlopen(fb_url).read()
    jsonResponse = json.loads(fanCount)
    return jsonResponse['fan_count']

def postToSlack():
    fb_fans = str(fanCount())
    data = '{"attachments":[{"fallback":"'+fb_page+' has '+fb_fans+' followers.","pretext":"'+fb_page+' has '+fb_fans+' followers.","color":"'+style+'","fields":[{"title":"Facebook Fans","value":"'+fb_page+' has '+fb_fans+' followers.","short":false}]}]}'
    slack = urllib2.Request(webhook, data, {'Content-Type': 'application/json'})
    f = urllib2.urlopen(slack)
    f.close()

postToSlack()

exit()