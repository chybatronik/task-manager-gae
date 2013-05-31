from google.appengine.ext import db
from google.appengine.api.users import User

class Company(db.Model):
    name = db.StringProperty(required=True)
    date = db.DateTimeProperty(auto_now_add=True)
    email = db.EmailProperty(required=True)
    atach_users = db.ListProperty(User)
    create_by = db.UserProperty(required=True)


class Task(db.Model):
    title = db.StringProperty(required=True)
    text = db.TextProperty()    
    is_done = db.BooleanProperty(default=False)    
    atach_users = db.ListProperty(User)
    date = db.DateTimeProperty(auto_now_add=True)
    create_by = db.UserProperty(required=True)