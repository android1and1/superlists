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

# after commit 'can returns html',first add
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://54.199.137.210:8080')
		# after commit 'can returns html',first add
		header_text = self.browser.find_element_by_tag_name('h1').text
		#self.assertIn('To-Do',self.browser.title)

		# after commit 'can returns html',first add
		self.assertIn('To-Do',header_text)

		# she is invited to enter a to-do lists 
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
				inputbox.get_attribute('placeholder'),'Enter a to-do item'
		)

		# she types 'buy peacock feathers' into a text box(Edith's hobby
		# is tying fly-fishing lures)
		inputbox.send_keys('Buy peacock feathers')
		# when she hits enter,the page updates,and now the page lists
		# "1:Buy peacock feathers" as an item in a to-do list table
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(any(row.text=='1:Buy peacock feathers' for row in rows))

		# there is still a text box inviting her to add another item.
		# she enters 'Use peacock feathers to make a fly'(Edith is very methodical)

		self.fail('finish the test!')
		# rest of comments.
if __name__ == '__main__':
	# original is "unittest.main(warnings='ignore')"
	#unittest.main()
	unittest.main(warnings='ignore')
