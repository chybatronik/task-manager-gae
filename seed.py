from controllers.base_controller import *
from google.appengine.api.users import User

class SeedPage(BaseRequestHandler):

    def get(self):
        self.seed_data()
        self.redirect("/tasks")

    def seed_data(debug=True):
        #delete all data
        if not debug:
            return True
        users = UserInsurance.all()
        for user in users:
            db.delete(user) 

        companies = Company.all()
        for company in companies:
            db.delete(company) 

        tasks = Task.all()
        for task in tasks:
            db.delete(task) 

        #create new instance

        user = User(email="test@example.com")
        user_insurance = UserInsurance(user=user).put()

        user2 = User(email="test2@example.com")
        user_insurance2 = UserInsurance(user=user2).put()

        user3 = User(email="test3@example.com")
        user_insurance2 = UserInsurance(user=user3).put()

        company1 = Company(name = "A-Z Group Ltd", create_by= user, email="Ltd@Group.com")
        company1.put()

        company2 = Company(name = "The Albany Engineering Co Ltd  ", create_by= user2, email="Albany@Engineering.com")
        company2.put()

        company3 = Company(name = "Alcoa Europe  ", create_by= user3, email="Alcoa@Europe.com")
        company3.put()

        Task(title = "Name tasks 1",
            text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",  
            create_by= user,
            attach_users = [user2, user3]).put()

        Task(title = "Name tasks 2",
            text = "On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. ",  
            create_by= user2,
            attach_users = [user2]).put()

        Task(title = "Name tasks 2",
            text = "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.",  
            create_by= user3,
            attach_users = [user, user2, user3]).put()
