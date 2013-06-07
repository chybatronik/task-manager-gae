from controllers.base_controller import *
from controllers.company_controller import *
from controllers.task_controller import *
from controllers.user_controller import *
from controllers.file_controller import *
from seed import *

_DEBUG = True

class IndexPage(BaseRequestHandler):

    def get(self):
        user = users.get_current_user()
        template_values = {
        }

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
    ('/tasks/(\d+)/blob/(.*)/delete', DeleteBlobFromTask),

    ('/users', AllUserInsurancePage),
    ('/users/(\d+)', ShowUserInsurancePage),
    ('/users/(\d+)/edit', EditUserInsurancePage),
    ('/users/invite', InviteUserInsurancePage),
    ('/users/(\d+)/delete', DeleteUserInsurancePage),

    ('/seed_data', SeedPage),

    ('/uploads', UploadHandler),
    ('/server', DownloadHandler)
    
], debug=_DEBUG)