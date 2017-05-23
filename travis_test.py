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
        submit_issue(self.title, msg, self.score)
        exit(1)
        
    def expect_contains(self, what, string, substr):
        if string is None:
            self.error("Expected {0} containing \"{1}\",  \nbut got `None`".format(what, substr))
        if substr not in string:
            self.error("Expected {0} to contain \"{1}\",  \nbut got \"{2}\".".format(what, substr, string))

    def expect_no_error(self, error):
        self.error("Failed, got exception:\n```\n{0}```".format(error))
        
    def reply_to(self, tweet):
        return reply({'text': tweet, 'user': {'screen_name': 'TestUser'}})

    def test_math1(self):
        """Given a tweet '1+1'. Then the bot's answer should contain '2'"""
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

	def test_math2(self):
		"""Given a tweet '1+2'. Then the bot's answer should contain '3'"""
		self.issue('The bot should be able to actually do maths, not relying on hard-coded values', 
		"""
Given a tweet \"1+2\",  
Then the bot's answer should contain \"3\".
		""")
		try:
			response = self.reply_to("1+2")
			self.expect_contains("response", response, "3")
		except Exception as ex:
			self.expect_no_error(traceback.format_exc())

	def test_math3(self):
		"""Given a tweet '1999+1'. Then the bot's answer should contain '2000'"""
		self.issue('The bot should be able to do maths with large numbers', 
		"""
Given a tweet \"1999+1\",  
Then the bot's answer should contain \"2000\".
		""")
		try:
			response = self.reply_to("1999+1")
			self.expect_contains("response", response, "2000")
		except Exception as ex:
			self.expect_no_error(traceback.format_exc())

#Given a tweet "2+3"
#Then the bot's answer should not contain any digits except "5"

#Given a tweet "Tell me about Chuck Norris"
#Then the bot's answer should contain a Chuck Norris fact

    #Given a tweet "@Bot 1+1"
    #Then the bot's answer should contain 2
    def test_mention(self):
        self.issue('The bot should ignore the @mention', 
        """
Given a tweet \"@Bot 1+1\",  
Then the bot's answer should contain \"2\".

* To check if a string starts with '@', you can use [`string.startswith('@')`](https://docs.python.org/2/library/stdtypes.html#str.startswith).
* To split a string after the first space, you can use [`string.split(' ', 1)`](https://docs.python.org/2/library/stdtypes.html#str.split).
        """)
        try:
            response = self.reply_to("@Bot 1+1")
            self.expect_contains("response", response, "2")
        except Exception as ex:
            self.expect_no_error(traceback.format_exc())









            
    # insert all tests above this line ------------
    def test_done(self):
        submit_issue('Concratulations, you have completed the exercise!', 
            'To disable these notifications, remove the `before_install` and `after_success` hooks from your `.travis.yml` file.', 
            self.score+1)
        exit(1)
            
if __name__ == '__main__':
    unittest.main(verbosity=2)
