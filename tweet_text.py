# Allows using time related functions
import time

def tweet_text():
  # Construct the text we want to tweet out (140 chars max)
  text = time.strftime("It is %H:%M:%S on a %A (%d-%m-%Y).")
  return text