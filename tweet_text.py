"""Construct messages to be sent as tweet text"""

# Allows using time related functions
from datetime import datetime
# convert times according to time zones
from pytz import timezone

def reply(tweet):
    """Return text to be used as a reply"""
    message = tweet['text']
    user = tweet['user']['screen_name']
    if "1+1" in message:
        return "@" + user + " 2"
    if "1+2" in message:
        return "@" + user + " 3"
    if "2+3" in message:
        return "@" + user + " 456"
    if "1999+1" in message:
        return "@" + user + " 2000"
    if "9000+1" in message:
        return "@" + user + " 9001 It's over nine thousand!"
    if "rly" in message:
        return "@" + user + " YA RLY!"
    pokemons = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise"]
    if "Pokemon" in message:
        number = message.split('#')[1]
        return "@" + user + " " + pokemons[int(number)-1]
        
    if "hi" in message.lower():
        berlin_time = datetime.now(timezone('Europe/Berlin'))
        date = berlin_time.strftime("It is %H:%M:%S on a %A (%d-%m-%Y).")
        return "Hi @" + user + "! " + date
    return None

def idle_text():
    """Return text that is tweeted when not replying"""
    # Construct the text we want to tweet out (140 chars max)
    berlin_time = datetime.now(timezone('Europe/Berlin'))
    text = berlin_time.strftime("It is %H:%M:%S on a %A (%d-%m-%Y).")
    return text
