# Allows using time related functions
import time

def reply(tweet):
    message = tweet['text']
    user = tweet['user']['screen_name']
    if "hi" in message.lower():
        return "Hi @" + user + "! " + time.strftime("It is %H:%M:%S on a %A (%d-%m-%Y).")
    else:
        return None

def idle_text():
    # Construct the text we want to tweet out (140 chars max)
    text = time.strftime("It is %H:%M:%S on a %A (%d-%m-%Y).")
    return text
