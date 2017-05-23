# https://docs.python.org/2/library/unittest.html
import unittest

from tweet_text import idle_text, reply
from travis.submit_issue import submit_issue
from sys import exit
import traceback

# The basic building blocks of unit testing are test cases
# single scenarios that must be set up and checked for correctness.
# In unittest, test cases are represented by instances of unittest's TestCase class.
# To make your own test cases you must write subclasses of TestCase.

class TestTasks(unittest.TestCase):

	def __init__(self, *args, **kwargs):
		super(TestTasks, self).__init__(*args, **kwargs)
		self.score = 0

	def issue(self, title, body):
		self.score = self.score + 1
		self.title = title
		self.body = body
		
	def error(self, message):
		msg = self.body + "\n\n>" + message
		print self.title
		print msg
		submit_issue(self.title, msg, self.score)
		exit(1)
		
	def expect_contains(self, what, string, substr):
		if substr not in string:
			self.error("Expected {0} to contain \"{1}\",  \nbut got \"{2}\".".format(what, substr, string))

	def expect_no_error(self, error):
		self.error("Failed, got exception:\n```\n{0}```".format(error))
		
	def reply_to(self, tweet):
		return reply({'text': tweet, 'user': {'screen_name': 'TestUser'}})

	def test_math1(self):
		self.issue('The bot should be able to do simple math', 
		"""
Given a tweet \"1+1\",  
Then the bot's answer should contain \"2\".

* To split the term into operands, you can use [`string.split('+')`](https://docs.python.org/2/library/stdtypes.html#str.split).
* To convert a  string to an integer, you can use [`int(string)`](https://docs.python.org/2/library/functions.html#int).
		""")
		try:
			response = self.reply_to("1+1")
			self.expect_contains("response", response, "2")
		except Exception as ex:
			self.expect_no_error(traceback.format_exc())
			

#Given a tweet "1+1"
#Then the bot's answer should contain "2"

#Given a tweet "What is 1+2?"
#Then the bot's answer should contain "3"

#Given a tweet "2+3"
#Then the bot's answer should contain "5"

#Given a tweet "2+3"
#Then the bot's answer should not contain any digits except "5"

#Given a tweet "Tell me about Chuck Norris"
#Then the bot's answer should contain a Chuck Norris fact

			
if __name__ == '__main__':
    unittest.main(verbosity=2)
