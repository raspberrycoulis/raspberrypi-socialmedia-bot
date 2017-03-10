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

# twitter.py
First, you'll need to create an app in Twitter. This sounds more complicated that it is, but you'll first need to go to `https://apps.twitter.com/` and then click the `Create New App` button at the top. You'll need to name your app and provide some required information along the way.

Once you've created your app, you'll need to generate a Consumer Key and Secret. You'll need this information to access the Twitter API. Click on the `Keys and Access Tokens` tab and then click generate under the `Access Tokens` section.

There are four keys you'll need for this script to work:

  1. Consumer Key
  2. Consumer Secret
  3. Access Token
  4. Access Token Secret

**Please keep these safe and secret!** 

# Slack Incoming Webhook
You'll also need to create an Incoming Webhook in Slack. [This page from Slack's API documentation](https://api.slack.com/incoming-webhooks) will provide all the information you need to get this up and running.

If you like, you can also customise the integration with a custom icon - in fact, there are two to use in the `img` folder within this repository if you want.