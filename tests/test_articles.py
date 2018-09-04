import unittest
from app.models import Articles

class TestArticles(unittest.TestCase):
    '''
    Test class to test the behavior of the articles class
    '''
    def setUp(self):
        '''
        Test class to run before other tests
        '''
        self.new_article = Articles('koyoo','sales is advanced','the marketing industry is realy transforming verry fast',
        'https://google.com','https://google.com/images','2015-01-10T36:20:07Z')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))
    
    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.author,'koyoo')
        self.assertEquals(self.new_article.title,'sales is advanced')
        self.assertEquals(self.new_article.description,'the marketing industry is realy transforming verry fast')
        self.assertEquals(self.new_article.url,'https://google.com')
        self.assertEquals(self.new_article.urlToImage,'https://google.com/images')
        
        