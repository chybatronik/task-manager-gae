import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

_DEBUG = True

ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
    extensions=['jinja2.ext.autoescape'])

class BaseRequestHandler(webapp2.RequestHandler):
    def generate(self, template_name, template_values={}):
        values = {
            'request': self.request,
            'user': users.get_current_user(),
            'nick_name':users.get_current_user().nickname(),
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

application = webapp2.WSGIApplication([
    ('/', IndexPage),
], debug=_DEBUG)