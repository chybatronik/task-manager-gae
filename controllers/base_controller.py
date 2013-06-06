import os

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext.blobstore import BlobInfo
from google.appengine.ext import blobstore

import jinja2
import webapp2

from models import *

_DEBUG = True

ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader("./templates"),#os.path.join(os.path.dirname(__file__), "templates")),
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
