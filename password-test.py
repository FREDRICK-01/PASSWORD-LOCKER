import unittest
from password import User
from password import Credentials


class TestClass(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """
    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('FredrickMwangi','ladhfdjgh')

    def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username,'FredrickMwangi')
        self.assertEqual(self.new_user.password,'ladhfdjgh')

    def test_save_user(self):
        """
        Test case to test if a new user instance has been saved into the User list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1) 


class TestCredentials(unittest.TestCase):
    """
    A test class that defines test cases for credentials class
    """ 
    def setUp(self):
        """
        Method that runs before each individual credentials test methods run.
        """
        self.new_credential = Credentials('G-mail','Fredrick_Mwangi','urewdsfghjh')
    def test_init(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credential.account,'G-mail')
        self.assertEqual(self.new_credential.userName,'Fredrick_Mwangi')
        self.assertEqual(self.new_credential.password,'urewdsfghjh') 
        
    def save_credential_test(self):
        """
        test case to test if the crential object is saved into the credentials list.
        """
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        '''
        method that cleans up after each test case has run.
        '''
        Credentials.credentials_list = []   

    def test_display_all_saved_credentials(self):
        '''
        method that displays all the credentials that has been saved by the user
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == "__main__":
    unittest.main()              
