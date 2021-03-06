from base_controller import *
from google.appengine.api import images
import cgi, re

class AllUserInsurancePage(BaseRequestHandler):
    def get(self):
        users = UserInsurance.all()
        template_values = {
            "users":users,
        }
        self.generate("users/index.html", template_values)

class InviteUserInsurancePage(BaseRequestHandler):
    def get (self, errors=None):
        template_values = {
            "errors":errors,
            "users":UserInsurance.all(),
        }
        self.generate("users/invite.html", template_values)

    def post(self):
        try:
            user = users.User(email=self.request.get("email"))
            user_insurance = UserInsurance(user=user)
            user_insurance.put()
            db.put(user_insurance)
            self.redirect("/users")
        except db.BadValueError, errors:
            self.get(errors)

class EditUserInsurancePage(BaseRequestHandler):
    def get (self, user_id, errors=None):
        template_values = {
            "errors":errors,
            "user_insurance":UserInsurance.get_by_id(int(user_id)),
        }
        self.generate("users/edit.html", template_values)


    def post(self, user_id):
        try:
            user_insurance = UserInsurance.get_by_id(int(user_id))

            user_insurance.put()
            db.put(user_insurance)
            self.redirect("/users/"+cgi.escape(user_id))
        except db.BadValueError, errors:
            self.get(int(user_id), errors)

class ShowUserInsurancePage(BaseRequestHandler):
    def get(self, user_id):
        template_values = {
            "user_insurance":UserInsurance.get_by_id(int(user_id)),
        }
        self.generate("users/show.html", template_values)

class DeleteUserInsurancePage(BaseRequestHandler):
    def post(self, user_id):
        user_insurance = UserInsurance.get_by_id(int(user_id))
        user_insurance.delete()
        db.delete(user_insurance.key())
        self.redirect("/users")
