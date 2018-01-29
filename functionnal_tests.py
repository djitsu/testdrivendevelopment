from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):


        # address to check
        self.browser.get('http://localhost:8000')
        
        # does ths page title mention that's it a to do list?
        self.assertIn('To-Do',self.browser.title)
        self.fail('Finish the test')
        
        # you can add a to do item
        
        # you type "buy peacock feathers" into a text box
        
        # when you click enter the page updates and tou have 
        # "1: Buy peackock feathers" as an item in a to-do list
        
        # There is an item to invite you to add another item
        # you enter "Use peacock feathers to make a fly"
        
        # The page updates again an now you can see both items on the list
        
        # Is the site will remember this list? you can see that website generate a unique 
        # Url for you -- some explanatory test to that effect
        
        # You visit that Url. your To-Do list still there

if __name__ == '__main__':
    unittest.main(warnings='ignore')
