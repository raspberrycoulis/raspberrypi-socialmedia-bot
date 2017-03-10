# Raspberry Pi Social Media Bot
Python scripts that check your Twitter and Facebook followers and sends you Slack notifications with the totals.

## Pre-Requisites
There are two Python scripts in here - one is for checking Twitter and the other for Facebook. To access Twitter's API, you will need to install Tweepy - Twitter for Python by doing the following:

    sudo pip install tweepy

If you do not have PIP installed on your Raspberry Pi, you can install this by running:

    sudo apt-get install python-pip python3-pip

## Clone this GitHub Repository
Once you have installed Tweepy, you will need to clone this repository, done simply by:

    git clone https://github.com/raspberrycoulis/raspberrypi-socialmedia-bot.git

You'll then need to add the necessary parts to each script as follows.

## Twitter App
First, you'll need to create an app in Twitter. This sounds more complicated that it is, but you'll first need to go to [https://apps.twitter.com/](https://apps.twitter.com/) and then click the `Create New App` button at the top. You'll need to name your app and provide some required information along the way.

Once you've created your app, you'll need to generate a Consumer Key and Secret. You'll need this information to access the Twitter API. Click on the `Keys and Access Tokens` tab and then click generate under the `Access Tokens` section.

There are four keys you'll need for this script to work:

  1. Consumer Key
  2. Consumer Secret
  3. Access Token
  4. Access Token Secret

**Please keep these safe and secret!** 

## Facebook App
Again, to access Facebook's API you will need some credentials. The process is very similar to creating the Twitter app above. Head over to [https://developers.facebook.com/apps/](https://developers.facebook.com/apps/) and `+ Add a New App`. Give your app a unique name and provide the required information when asked. You'll then be given an App ID and an App Secret. Again, **keep this safe and secret** but they will form part of our code in `facebook.py` later on.

### Facebook Page ID
You will only be able to check a Facebook Page with `facebook.py`, **not** a Facebook Profile. To find out your Facebook Page ID, head over to [Find You Facebook ID](http://findmyfbid.com/) and enter the URL of your Facebook Page, i.e. `https://www.facebook.com/raspberrycoulis` and you'll be given a unique string of numbers. This is your Facebook Page ID, so take note.

## Slack Incoming Webhooks
You'll also need to create an Incoming Webhook in Slack. [This page from Slack's API documentation](https://api.slack.com/incoming-webhooks) will provide all the information you need to get this up and running.

If you like, you can also customise the integration with a custom icon - in fact, there are two to use in the [img](https://github.com/raspberrycoulis/raspberrypi-socialmedia-bot/tree/master/img) folder within this repository if you want.

I would advise creating two different webhooks - one for the Twitter bot and one for the Facebook bot, but you do not need to if you don't want to.

Copy the webhooks as you'll need this in `twitter.py` and `facebook.py` respectively.

# Updating your Python scripts
Now you should have all the required information to get these Python scripts working. You now need to add them to the relevant Python scipt in the places pointed out by the comments I have added. 

## twitter.py
Add your consumer key, consumer secret, access token and access token secret in the correct place (making sure you keep the '' present) and then add your Slack webhook too. You will then need to specify the username of the account you want to check the follower count of, but ignore the @ pre-fix - i.e. `raspberrycoulis`. To make this look nicer in the Slack notification, you can add the name again in the `handle` section.

You can also specify the colour displayed in the Slack notification by changing the style here. You can use any hex colour code to your liking.

### Timing
The `twitter.py` script includes sections that are currently commented out by default. If you wanted to, you can delete the # before `while True` and `time.sleep(wait)` and then commenting out (adding a #) in front of `exit()` and the script will then run based on the `wait` variable specifed. I have commented these sections out as you may prefer to schedule the script to run at set times during the day using a crontab.