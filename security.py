from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    print ('authenticate')
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user
    
def identity(payload):
    print ('identity')
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)