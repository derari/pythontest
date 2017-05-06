#!/usr/bin/env python

#
# IMPORTS
#

# basic operating system interactions
import os
import sys
# pretty print variables, show them with newlines, so that they are readable
from pprint import pprint
# import the code that connects to Twitter
from twython import Twython
# http://apscheduler.readthedocs.io/en/3.3.1/
from apscheduler.schedulers.blocking import BlockingScheduler
# import the 'tweet_text' function from tweet_text.py
from tweet_text import tweet_text

# Try to import the variables defined in credentials.py
# If that does not exist (e.g. on Heroku), fall back to environment variables
try:
    from credentials import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
except ImportError as error:
    print 'Info: {e}'.format(e=error)
    print 'Info: Cannot load credentials.py. Will use environment variables.'
    try:
        APP_KEY = os.environ['APP_KEY']
        APP_SECRET = os.environ['APP_SECRET']
        OAUTH_TOKEN = os.environ['OAUTH_TOKEN']
        OAUTH_TOKEN_SECRET = os.environ['OAUTH_TOKEN_SECRET']
    except KeyError as error:
        print 'Error: {e} not found in environment variables'.format(e=error)
        print 'Error: Could not retrieve credentials from either credentials.py or environment variables. Make sure either is set.'
        # can't do anything without credentials, so quit
        sys.exit()


#
# BOT CODE
#

# Login to Twitter
account = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Check the supplied credentials, get some general info on the account
# https://dev.twitter.com/rest/reference/get/account/verify_credentials
info = account.verify_credentials(include_entities=False, skip_status=True, include_email=False)

# pprint(info)
print 'user:', info['screen_name']
print 'tweet count:', info['statuses_count']
print 'favourite count:', info['favourites_count']
print 'friends count:', info['friends_count']

scheduler = BlockingScheduler()
interval_minutes = 10

@scheduler.scheduled_job('interval', minutes=interval_minutes)
def regular_tweet():
  # from tweet_text.py
  text = tweet_text()
  # Send the tweet!
  tweet = account.update_status(status=text)
  # Print some info on the sent tweet
  # pprint(tweet)
  print 'https://twitter.com/statuses/{id}'.format(id=tweet['id'])

try:
    print 'Info: {name} running.'.format(name=sys.argv[0])
    print 'Info: Will tweet every {min} minutes. Stop with Ctrl+c'.format(min=interval_minutes)
    scheduler.start()
# a KeyboardInterrupt exception is generated when the user presses Ctrl+c
except KeyboardInterrupt:
    print '\nInfo: Shutting down. Bye!'
