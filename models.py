from google.appengine.ext import db

class Company(db.Model):
	name = db.StringProperty(required=True)
	date = db.DateTimeProperty(auto_now_add=True)
	create_by = db.UserProperty(required=True)


class TestModel(db.Model):
    pass