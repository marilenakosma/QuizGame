from tinydb import TinyDB,Query
from datetime import datetime

users_table = TinyDB('users.json')
scores_table=TinyDB('scores.json')
User = Query()


def save_user(username:str, password:str) -> bool:
   if not users_table.search(Query().username == username):
       users_table.insert({"username":username,"password":password})
       return True
   return False

def authenticate_user(username:str, password:str) -> bool:
   return users_table.contains((User.username == username) & (User.password == password))

def get_user(username:str):
    return users_table.get(User.username == username)

def save_score(username:str,score:int,category:str = None,date=None):
    scores_table.insert({
        "username":username,
        "score":score,
        "category":category,
        "date":date if date else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

def get_scores(username:str):
    return scores_table.search(User.username == username)

