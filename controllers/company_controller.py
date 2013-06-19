from base_controller import *

class AllCategoryPage(BaseRequestHandler):
    def get(self):
        companies = Category.all()
        template_values = {
            "companies":companies,
        }
        self.generate("company/index.html", template_values)

class ShowCategoryPage(BaseRequestHandler):
    def get(self, company_id ):
        template_values = {
            "company":Category.get_by_id(int(company_id)),
        }
        self.generate("company/show.html", template_values)

class CreateCategoryPage(BaseRequestHandler):
    def get (self, errors=None):
        template_values={
            "users":UserInsurance.all(),
            "errors":errors,
        }
        self.generate("company/new.html", template_values)

    def post(self):
        try:
            users_u =  self.request.get_all("users")
            users_array = []
            for user in users_u:
                users_array.append(UserInsurance.get_by_id(int(user)).user)

            com = Category(name = self.request.get("name"), email = self.request.get("email"), 
                create_by = users.get_current_user(), attach_users = users_array)
            com.put()
            db.put(com)
            self.redirect("/companies/" + str(com.id()))  
        except db.BadValueError, errors:
            self.get(errors)

class EditCategoryPage(BaseRequestHandler):
    def get(self, company_id, errors=None):
        template_values = {
            "company":Category.get_by_id(int(company_id)),
            "errors": errors,
            "users":UserInsurance.all(),
        }

        self.generate("company/edit.html", template_values)

    def post(self, company_id):
        try:
            users_u =  self.request.get_all("users")
            users_array = []
            for user in users_u:
                users_array.append(UserInsurance.get_by_id(int(user)).user)

            com = Category.get_by_id(int(company_id))
            com.name = self.request.get("name")
            com.email = self.request.get("email")
            com.attach_users = users_array
            com.put()
            db.put(com)
            self.redirect("/companies/" + str(com.key().id()))
        except db.BadValueError, errors:
            self.get(int(company_id), errors)


class DeleteCategoryPage(BaseRequestHandler):
    def post(self, company_id):
        com = Category.get_by_id(int(company_id))
        com.delete()
        db.delete(com.key())
        self.redirect("/companies")
