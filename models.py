from re import match, IGNORECASE, UNICODE, VERBOSE
from google.appengine.ext import db
from google.appengine.api.users import User

def valid_email(email):
    if not email:
        raise db.BadValueError('Please enter an email address')

    if len(email) > 75:
        raise db.BadValueError('Email address must be 6-75 characters long')

    if not match(r'''
        ^
        [\w.%+-]{1,75}
        @
        [a-z\d.-]{1,75}
        \.
        [a-z]{2,4}
        $
        ''', email, IGNORECASE | VERBOSE):
        raise db.BadValueError('Invalid email address')

class Company(db.Model):
    name = db.StringProperty(required=True)
    date = db.DateTimeProperty(auto_now_add=True)
    email = db.EmailProperty(required=True, validator=valid_email)
    atach_users = db.ListProperty(User)
    create_by = db.UserProperty(required=True)

    


class Task(db.Model):
    title = db.StringProperty(required=True)
    text = db.TextProperty()
    is_done = db.BooleanProperty(default=False)
    atach_users = db.ListProperty(User)
    priority = db.RatingProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    create_by = db.UserProperty(required=True)
    company = db.ReferenceProperty(Company, required=True)