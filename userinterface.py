from password import User, Credentials
function()

def create_new_user(username,password):
    """ 
    Function to create a new user with a new username and password.
    """
    new_user = User(username,password)
    return new_user


def save_user(user):
    """
    Function to save a ner user
    """
    user.save_user()


def display_user():
    """
     Function to display an existing user.
    """
    return User.display_user()  

def login_user(username,password):
    """
    function that checks whether a user exist and then login the user in.
    """
  
    check_user = Credentials.verify_user(username,password)
    return 

def create_new_credential(account,userName,password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credentials(account,userName,password)
    return new_credential
def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials. save_details()
def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list.
    """
    credentials.delete_credentials()

def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the credentials that belong to that account
    """
    return Credentials.find_credential(account)
def check_credendtials(account):
    """
    Function that check if  credentials exists with that account name and return true or false.
    """
    return Credentials.if_credential_exist(account)    

def generate_Password():
    """
    Generates a random password for the user.
    """
    auto_password=Credentials.generatePassword()
    return auto_password
def copy_password(account):
    """
    A function that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    return Credentials.copy_password(account)
