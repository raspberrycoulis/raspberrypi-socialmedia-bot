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

## Configuration File
To keep things simple, I have created a global `config.py` file that you will need to update before **any** script will work. You will need to add the relevant webhooks, API keys, tokens, secrets, account names and ID's etc. in this file first. Further instructions are given in the comments of this file.

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

## Instagram App and Access Token
You will need to create an app over at [https://www.instagram.com/developer/](https://www.instagram.com/developer/) in order to get access to the API. Once you have an app, head on over to [http://jelled.com/instagram/access-token](http://jelled.com/instagram/access-token) in order to generate your Access Token.

## Slack Incoming Webhooks
You'll also need to create an Incoming Webhook in Slack. [This page from Slack's API documentation](https://api.slack.com/incoming-webhooks) will provide all the information you need to get this up and running.

If you like, you can also customise the integration with a custom icon - in fact, there are two to use in the [img](https://github.com/raspberrycoulis/raspberrypi-socialmedia-bot/tree/master/img) folder within this repository if you want.

I would advise creating two different webhooks - one for the Twitter bot and one for the Facebook bot, but you do not need to if you don't want to.

Copy the webhooks as you'll need this in `twitter.py` and `facebook.py` respectively.

# Make each script executable
Do this by typing the following into the terminal (assuming you are in the `raspberrypi-socialmedia-bot` folder):

    chmod +x twitter.py facebook.py instagram.py config.py

## Run the scripts
Test the scripts out by running either:

    ./twitter.py

or

    ./facebook.py
    
or

    ./instagram.py
    
If successful, you should receive a Slack notification for each telling you how many Twitter followers you have, how many Facebook Fans you have and finally the number of Instagram followers you have.

You can now automate them using cron, and I highly recommend [crontab.guru](https://crontab.guru/) if you need help generating the relevant command. I currently run my twice daily - at 10am and 10pm for `twitter.py`, 10:05am and 10:05pm for `facebook.py` and 10:10am and 10:10pm for `instagram.py`.