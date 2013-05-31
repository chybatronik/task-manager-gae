import os

from google.appengine.api import users
from google.appengine.ext import db

import jinja2
import webapp2
from models import *

_DEBUG = True

ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
    extensions=['jinja2.ext.autoescape'])

class BaseRequestHandler(webapp2.RequestHandler):
    def generate(self, template_name, template_values={}):
        values = {
            'request': self.request,
            'user': users.get_current_user(),
            'login_url': users.create_login_url(self.request.uri),
            'url_sing_out': users.create_logout_url('http://%s/' % (
                self.request.host))}
        values.update(template_values)
        template = ENV.get_template(template_name)
        self.response.out.write(template.render(values, debug=_DEBUG))

class IndexPage(BaseRequestHandler):

    def get(self):
        user = users.get_current_user()
        template_values = {
        }

        template = ENV.get_template('index.html')
        self.generate("index.html", template_values)

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
    def post(self, company_id = None):
        com = Company(name = self.request.get("name"), email = self.request.get("email"), 
            create_by = users.get_current_user()).put()
        self.redirect("/companies")  

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


class DeleteCompanyPage(BaseRequestHandler):
    def post(self, company_id):
        com = Company.get_by_id(int(company_id))
        db.delete(com)
        self.redirect("/companies") 

application = webapp2.WSGIApplication([
    ('/', IndexPage),
    ('/companies', AllCompanyPage),
    ('/companies/create', CreateCompanyPage),
    ('/companies/(\d+)', ShowCompanyPage),
    ('/companies/(\d+)/edit', EditCompanyPage),
    ('/companies/(\d+)/delete', DeleteCompanyPage),
    
], debug=_DEBUG)