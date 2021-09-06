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
    return check_user      
