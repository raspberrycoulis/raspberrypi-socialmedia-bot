#!/usr/bin/python

import urllib2
from urllib import quote
import json
from config import (
    fb_webhook,
    fb_id,
    fb_app_id,
    fb_secret,
    fb_style,
    fb_page
)

# The functions that creates the magic - checks your Facebook Company Page for the number of fans then sends this data to Slack to notify you.

def fanCount():
    fb_url = 'https://graph.facebook.com/{}?access_token={}|{}&fields=fan_count'.format(quote(fb_id), quote(fb_app_id), quote(fb_secret))
    fanCount = urllib2.urlopen(fb_url).read()
    jsonResponse = json.loads(fanCount)
    return jsonResponse['fan_count']

def postToSlack():
    fb_fans = str(fanCount())
    data = '{"attachments":[{"fallback":"'+fb_page+' has '+fb_fans+' followers.","pretext":"'+fb_page+' has '+fb_fans+' followers.","color":"'+fb_style+'","fields":[{"title":"Facebook Fans","value":"'+fb_page+' has '+fb_fans+' followers.","short":false}]}]}'
    slack = urllib2.Request(fb_webhook, data, {'Content-Type': 'application/json'})
    f = urllib2.urlopen(slack)
    f.close()

postToSlack()

exit()