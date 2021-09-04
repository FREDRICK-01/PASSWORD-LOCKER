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

       