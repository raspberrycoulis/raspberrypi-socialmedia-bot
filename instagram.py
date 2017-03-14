#!/usr/bin/python

import urllib2
from urllib import quote
import json
from config import (
    ig_style,
    ig_account,
    ig_access_token,
    ig_webhook
)

def fanCount():
        ig_url = 'https://api.instagram.com/v1/users/self/?access_token={}'.format(quote(ig_access_token))
        fanCount = urllib2.urlopen(ig_url).read()
        jsonResponse = json.loads(fanCount)
        return jsonResponse['data']['counts']['followed_by']

def postToSlack():
        ig_followers = str(fanCount())
        data = '{"attachments":[{"fallback":"'+ig_account+' has '+ig_followers+' followers.","pretext":"'+ig_account+' has '+ig_followers+' followers.","color":"'+ig_style+'","fields":[{"title":"Instagram Followers","value":"'+ig_account+' has '+ig_followers+' followers.","short":false}]}]}'
        slack = urllib2.Request(ig_webhook, data, {'Content-Type': 'application/json'})
        f = urllib2.urlopen(slack)
        f.close()

postToSlack()

exit()