from base_controller import *
from company_controller import *
from task_controller import *

_DEBUG = True


class IndexPage(BaseRequestHandler):

    def get(self):
        user = users.get_current_user()
        template_values = {
        }

        template = ENV.get_template('index.html')
        self.generate("index.html", template_values)


application = webapp2.WSGIApplication([
    ('/', IndexPage),
    ('/companies', AllCompanyPage),
    ('/companies/create', CreateCompanyPage),
    ('/companies/(\d+)', ShowCompanyPage),
    ('/companies/(\d+)/edit', EditCompanyPage),
    ('/companies/(\d+)/delete', DeleteCompanyPage),

    ('/tasks', AllTaskPage),
    ('/tasks/create', CreateTaskPage),
    ('/tasks/(\d+)', ShowTaskPage),
    ('/tasks/(\d+)/edit', EditTaskPage),
    ('/tasks/(\d+)/delete', DeleteTaskPage),
    
], debug=_DEBUG)