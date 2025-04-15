from tinydb import TinyDB,Query

db = TinyDB('db.json')
User = Query()

def add_user(username,password):
    db.insert({'username': username,'password':password})

def get_user(username):
    return db.get(User.username == username)

def user_exists(username):
    return db.contains(User.username == username)
def save_user(username:str, password:str):
    User = Query()


