from _typeshed import Self
import random
import string
class User: 
    """
    Creates a user class to generate a new instances.

    """
    user_list = []
    def __init__(self,username,password): 
        """
        This's a method that defines the properties of a user.

        """
        self.username = username
        self.password = password

    def save_user (self):
        """
        This's a method that sves a new user into the user list.
        """    
        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        return cls.user_list 

    def delete_user(cls):
        """
        Deletes a saved account from the list.
        """
        User.user_list.remove(self)
    
class Credentials():
    """
    This class helps in creation of new objects of Credentials. 
    """    
    credentials_list = []
    @classmethod
    def verify_user(cls,username,password):
        """
        Veryfies whether the user is in user_list or not.
        """
        a_user = ""
    def __init__(self,account,userName,password):
        """
        Method that defines user credentials to be stored.
        """
        self.account = account
        self.username = userName
        self.password = password

    def save_details(self):
        """
        Method to store new credential to the credentials list.
        """  
        Credentials.credentials_list.append(self)