from base_controller import *

class AllUserInsurancePage(BaseRequestHandler):
    def get(self):
        rpc = db.create_rpc(deadline=0.001, read_policy=db.STRONG_CONSISTENCY)
        users = UserInsurance.all().fetch(10, rpc=rpc)
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
            rpc = db.create_rpc(deadline=0.001, read_policy=db.STRONG_CONSISTENCY)
            db.put(user_insurance,  rpc=rpc)
            self.redirect("/users")
        except db.BadValueError, errors:
            self.get(errors)

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