# https://docs.python.org/2/library/unittest.html
import unittest

from tweet_text import idle_text, reply
from travis.submit_issue import submit_issue
from sys import exit
import traceback
import os

# The basic building blocks of unit testing are test cases
# single scenarios that must be set up and checked for correctness.
# In unittest, test cases are represented by instances of unittest's TestCase class.
# To make your own test cases you must write subclasses of TestCase.

class TestTasks:

    def __init__(self):
        self.score = 0
        
    def run(self):
        self.test_math1()
        self.test_math2()
        self.test_math3()
        self.test_mention()
        self.test_over9000()
        
        self.test_pokemon1()
        self.test_pokemon2()
        self.test_pokemon3()
        self.test_pokemon4()
        self.test_pokemon5()
        self.test_pokemon6()
        self.test_pokemon7()
        self.test_pokemon8()
        self.test_pokemon9()
        
        self.test_done()

    def issue(self, title, body):
        self.score = self.score + 1
        self.title = title
        self.body = body
        print title
        
    def error(self, message):
        msg = self.body + "\n\n>" + message
        if os.environ.get('TRAVIS_REPO_SLUG') is not None:
            submit_issue(self.title, msg, self.score)
        else:
            print "ERROR"
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
        except SystemExit:
            exit(1)
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
        except SystemExit:
            exit(1)
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
        except SystemExit:
            exit(1)
        except Exception as ex:
            self.expect_no_error(traceback.format_exc())

    def test_mention(self):
        """Given a tweet '@Bot 1+1'. Then the bot's answer should contain 2"""
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
        except SystemExit:
            exit(1)
        except Exception as ex:
            self.expect_no_error(traceback.format_exc())

    def test_over9000(self):
        """Given a tweet '@Bot 9000+1'. Then the bot's answer should contain '9001'
        and the string 'It's over nine thousand!'"""
        self.issue('The bot should ignore the @mention', 
        """
Given a tweet \"@Bot 9000+1\",
Then the bot's answer should contain \"9001\" and \"It's over nine thousand!\".
        """)
        try:
            response = self.reply_to("@Bot 9000+1")
            self.expect_contains("response", response, "9001")
            self.expect_contains("response", response, "It's over nine thousand!")
        except SystemExit:
                exit(1)
        except Exception as ex:
            self.expect_no_error(traceback.format_exc())

#Given a tweet "2+3"
#Then the bot's answer should not contain any digits except "5"

#Given a tweet "Tell me about Chuck Norris"
#Then the bot's answer should contain a Chuck Norris fact


# Bulbasaur, Ivysaur, Venusaur, Charmander, Charmeleon, Charizard, Squirtle, Wartortle, Blastoise

    def test_pokemon1(self):
        self.issue('The bot should know some Pokemon', 
        """
Given a tweet \"Which Pokemon is #1\",  
Then the bot's answer should contain \"Bulbasaur\".

* It's enough if the bot knows Pokemon #1 to #9
        """)
        try:
            response = self.reply_to("Which Pokemon is #1")
            self.expect_contains("response", response, "Bulbasaur")
        except SystemExit:
            exit(1)
        except Exception as ex:
            self.expect_no_error(traceback.format_exc())

    def test_pokemon2(self):
        self.issue('The bot should know Ivysaur', 
        """
Given a tweet \"Which Pokemon is #2\",  
Then the bot's answer should contain \"Ivysaur\".

* It's enough if the bot knows Pokemon #1 to #9
        """)
        try:
            response = self.reply_to("Which Pokemon is #2")
            self.expect_contains("response", response, "Ivysaur")
        except SystemExit:
            exit(1)
        except Exception as ex:
            self.expect_no_error(traceback.format_exc())
            
    def test_pokemon3(self):
        self.issue('The bot should know Venusaur', 
        """
Given a tweet \"Which Pokemon is #3\",  
Then the bot's answer should contain \"Venusaur\".

* It's enough if the bot knows Pokemon #1 to #9
        """)
        try:
            response = self.reply_to("Which Pokemon is #3")
            self.expect_contains("response", response, "Venusaur")
        except SystemExit:
            exit(1)
        except Exception as ex:
            self.expect_no_error(traceback.format_exc())
            
    def test_pokemon4(self):
        self.issue('The bot should know Charmander', 
        """
Given a tweet \"Which Pokemon is #4\",  
Then the bot's answer should contain \"Charmander\".

* It's enough if the bot knows Pokemon #1 to #9
        """)
        try:
            response = self.reply_to("Which Pokemon is #4")
            self.expect_contains("response", response, "Charmander")
        except SystemExit:
            exit(1)
        except Exception as ex:
            self.expect_no_error(traceback.format_exc())
            
    def test_pokemon5(self):
        self.issue('The bot should know Charmeleon', 
        """
Given a tweet \"Which Pokemon is #5\",  
Then the bot's answer should contain \"Charmeleon\".

* It's enough if the bot knows Pokemon #1 to #9
        """)
        try:
            response = self.reply_to("Which Pokemon is #5")
            self.expect_contains("response", response, "Charmeleon")
        except SystemExit:
            exit(1)
        except Exception as ex:
            self.expect_no_error(traceback.format_exc())
            
    def test_pokemon6(self):
        self.issue('The bot should know Charizard', 
        """
Given a tweet \"Which Pokemon is #6\",  
Then the bot's answer should contain \"Charizard\".

* It's enough if the bot knows Pokemon #1 to #9
        """)
        try:
            response = self.reply_to("Which Pokemon is #6")
            self.expect_contains("response", response, "Charizard")
        except SystemExit:
            exit(1)
        except Exception as ex:
            self.expect_no_error(traceback.format_exc())
            
    def test_pokemon7(self):
        self.issue('The bot should know Squirtle', 
        """
Given a tweet \"Which Pokemon is #7\",  
Then the bot's answer should contain \"Squirtle\".

* It's enough if the bot knows Pokemon #1 to #9
        """)
        try:
            response = self.reply_to("Which Pokemon is #7")
            self.expect_contains("response", response, "Squirtle")
        except SystemExit:
            exit(1)
        except Exception as ex:
            self.expect_no_error(traceback.format_exc())
            
    def test_pokemon8(self):
        self.issue('The bot should know Wartortle', 
        """
Given a tweet \"Which Pokemon is #8\",  
Then the bot's answer should contain \"Wartortle\".

* It's enough if the bot knows Pokemon #1 to #9
        """)
        try:
            response = self.reply_to("Which Pokemon is #8")
            self.expect_contains("response", response, "Wartortle")
        except SystemExit:
            exit(1)
        except Exception as ex:
            self.expect_no_error(traceback.format_exc())
            
    def test_pokemon9(self):
        self.issue('The bot should know Blastoise', 
        """
Given a tweet \"Which Pokemon is #9\",  
Then the bot's answer should contain \"Blastoise\".

* It's enough if the bot knows Pokemon #1 to #9
        """)
        try:
            response = self.reply_to("Which Pokemon is #9")
            self.expect_contains("response", response, "Blastoise")
        except SystemExit:
            exit(1)
        except Exception as ex:
            self.expect_no_error(traceback.format_exc())



            
    # insert all tests above this line ------------
    def test_done(self):
        submit_issue('Congratulations, you have completed the exercise!', 
            'To disable these notifications, remove the `before_install` and `after_success` hooks from your `.travis.yml` file.', 
            self.score+1)
        exit(1)


if __name__ == '__main__':
    TestTasks().run()
