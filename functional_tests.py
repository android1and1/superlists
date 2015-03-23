# not run this in acturely server! it is for client(installed python3 and selenium)
# raw functional test.

#from selenium import webdriver 

#browser = webdriver.Firefox()
#
## Edith has heard about a cool new online to-do app.....
#
## because nginx+gunicorn involeds too many things(static,media,etc..)
## so i decided use django's runserver first.
## browser.get('http://54.199.137.210')
#browser.get('http://54.199.137.210:8080')
#
##assert 'Django' in browser.title
#assert 'To-Do' in browser.title
## gracefully close firefox.exe.
#browser.quit()

from selenium import webdriver 
# now a new change:import builin module:unitest
import unittest
class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://54.199.137.210:8080')
		self.assertIn('To-Do',self.browser.title)
		self.fail('finish the test!')
		# rest of comments.
if __name__ == '__main__':
	# original is "unittest.main(warnings='ignore')"
	#unittest.main()
	unittest.main(warnings='ignore')



