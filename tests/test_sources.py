import unittest
from app.models import Sources

class SourcesTest(unittest.TestCase):
    '''
    Test case to test the behavior of the Sources class
    '''
    def setUp(self):
        '''
        Setup function that will run before every test
        '''
        self.new_source = Sources('news','the star','latest updates',
        'https://google.com','politics','kenya')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

    def test_to_check_instance_variables(self):
        '''
        Test function to check instance variables
        '''
        self.assertEquals(self.new_source.id,'news')
        self.assertEquals(self.new_source.name,'the star')
        self.assertEquals(self.new_source.description,'latest updates')
        self.assertEquals(self.new_source.url,'https://google.com')
        self.assertEquals(self.new_source.category,'politics')
        self.assertEquals(self.new_source.country,'kenya')