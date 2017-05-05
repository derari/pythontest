#!/usr/bin/env python

# import the code that connects to Twitter
from twython import Twython
# pretty print variables, show them with newlines, so that they are readable
from pprint import pprint
# http://apscheduler.readthedocs.io/en/3.3.1/
from apscheduler.schedulers.blocking import BlockingScheduler

# import all the variables defined in credentials.py
from credentials import *
# import the 'tweet_text' function from tweet_text.py
from tweet_text import tweet_text

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

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=3)
def regular_tweet():
  # from tweet_text.py
  text = tweet_text()
  # Send the tweet!
  tweet = account.update_status(status=text)
  # Print some info on the sent tweet
  # pprint(tweet)
  print 'https://twitter.com/statuses/{id}'.format(id=tweet['id'])

sched.start()
