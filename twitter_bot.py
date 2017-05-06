#!/usr/bin/env python

# import the code that connects to Twitter
from twython import Twython
# pretty print variables, show them with newlines, so that they are readable
from pprint import pprint
# http://apscheduler.readthedocs.io/en/3.3.1/
from apscheduler.schedulers.blocking import BlockingScheduler

from datetime import datetime

# import all the variables defined in credentials.py
from credentials import *
# import the 'tweet_text' function from tweet_text.py
from tweet_text import *

# Login to Twitter
account = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Check the supplied credentials, get some general info on the account
# https://dev.twitter.com/rest/reference/get/account/verify_credentials
info = account.verify_credentials(include_entities=False, skip_status=True, include_email=False)

# pprint(info)
print('user:', info['screen_name'])
print('tweet count:', info['statuses_count'])
print('favourite count:', info['favourites_count'])
print('friends count:', info['friends_count'])

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=10)
def regular_tweet():
  replied = False
  now = datetime.utcnow()
  for tweet in account.get_mentions_timeline():
    # for each mention
    time = datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
    delta = datetime.utcnow() - time
    # if it was less than 10 minutes ago
    if delta.days == 0 and delta.seconds < 600:
      # get reply from tweet_text.py
      reply_text = reply(tweet)
      if reply_text is not None:
        replied = True
        print('Replying to https://twitter.com/statuses/{id}'.format(id=tweet['id']))
        tweet = account.update_status(status=reply_text)
        print('https://twitter.com/statuses/{id}'.format(id=tweet['id']))
  if not replied:
    # from tweet_text.py
    text = idle_text()
    # Send the tweet!
    tweet = account.update_status(status=text)
    # Print some info on the sent tweet
    # pprint(tweet)
    print('https://twitter.com/statuses/{id}'.format(id=tweet['id']))

sched.start()