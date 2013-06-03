from base_controller import *

class AllTaskPage(BaseRequestHandler):
    def get(self):
        tasks = Task.all()
        template_values = {
            "tasks":tasks,
        }
        self.generate("task/index.html", template_values)

class ShowTaskPage(BaseRequestHandler):
    def get(self, task_id ):
        template_values = {
            "task":Task.get_by_id(int(task_id)),
        }
        self.generate("task/show.html", template_values)

class CreateTaskPage(BaseRequestHandler):
    def get (self, errors=None):
        template_values = {
            "companies":Company.all(),
            "errors":errors,
            "users":UserInsurance.all(),
        }
        self.generate("task/new.html", template_values)

    def post(self):
        try:
            company = Company.get_by_id(int(self.request.get("company")))
            task = Task(title = self.request.get("title"), text = self.request.get("text"), 
                create_by = users.get_current_user(), company = company).put()
            self.redirect("/tasks/" + str(task.id()))  
        except db.BadValueError, errors:
            self.get(errors)

class EditTaskPage(BaseRequestHandler):
    def get(self, task_id, errors=None):
        template_values = {
            "task":Task.get_by_id(int(task_id)),
            "companies":Company.all(),
        }
        self.generate("task/edit.html", template_values)

    def post(self, task_id):
        try:
            company = Company.get_by_id(int(self.request.get("company")))
            task = Task.get_by_id(int(task_id))
            task.title = self.request.get("title")
            task.text = self.request.get("text")
            task.company = company
            task.put()
            self.redirect("/tasks/" + str(task.key().id())) 
        except db.BadValueError, errors:
            self.get(int(task_id), errors)

class DeleteTaskPage(BaseRequestHandler):
    def post(self, task_id):
        task = Task.get_by_id(int(task_id))
        db.delete(task)
        self.redirect("/tasks") 