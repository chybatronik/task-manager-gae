from base_controller import *

class AllCompanyPage(BaseRequestHandler):
    def get(self):
        companies = Company.all()
        template_values = {
            "companies":companies,
        }
        self.generate("company/index.html", template_values)

class ShowCompanyPage(BaseRequestHandler):
    def get(self, company_id ):
        template_values = {
            "company":Company.get_by_id(int(company_id)),
        }
        self.generate("company/show.html", template_values)

class CreateCompanyPage(BaseRequestHandler):
    def get (self):
        self.generate("company/new.html", {})

    def post(self):
        com = Company(name = self.request.get("name"), email = self.request.get("email"), 
            create_by = users.get_current_user()).put()
        self.redirect("/companies/" + str(com.id()))  

class EditCompanyPage(BaseRequestHandler):
    def get(self, company_id):
        template_values = {
            "company":Company.get_by_id(int(company_id)),
        }
        self.generate("company/edit.html", template_values)

    def post(self, company_id):
        com = Company.get_by_id(int(company_id))
        com.name = self.request.get("name")
        com.email = self.request.get("email")
        com.put()
        self.redirect("/companies/" + str(com.key().id())) 


class DeleteCompanyPage(BaseRequestHandler):
    def post(self, company_id):
        com = Company.get_by_id(int(company_id))
        db.delete(com)
        self.redirect("/companies") 
