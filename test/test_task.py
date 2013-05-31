import unittest
from google.appengine.ext import db
from google.appengine.api.users import User
from google.appengine.ext import testbed
from google.appengine.datastore import datastore_stub_util

from main import *

class TaskTestCase(unittest.TestCase):

  def setUp(self):
    self.testbed = testbed.Testbed()
    self.testbed.activate()
    self.testbed.init_datastore_v3_stub()
    self.testbed.init_memcache_stub()

  def tearDown(self):
    self.testbed.deactivate()

  def testTask(self):
    user = User(email = "test@foo.com")

    company1 = Company(name = "Name", create_by= user, email="asdd@asdasd.com")
    company1.put()

    task1 = Task(title = "Name", create_by= user, company = company1)
    task1.put()
    task2 = Task(title = "Name", create_by= user, company = company1)
    task2.put()

    self.assertEqual(2, len(Task.all().fetch(2)))

  def test_without_name_Task(self):  
    user = User(email = "test@foo.com")
    company1 = Company(name = "Name", create_by= user, email="asdd@asdasd.com")
    company1.put()
    self.assertRaises(db.BadValueError, Task, create_by= user, company = company1)

  def test_without_user_Task(self):  
    user = User(email = "test@foo.com")
    company1 = Company(name = "Name", create_by= user, email="asdd@asdasd.com")
    company1.put()
    self.assertRaises(db.BadValueError, Task, title= "asdasd", company = company1)

  def test_default_id_done_Task(self):  
    user = User(email = "test@foo.com")
    company1 = Company(name = "Name", create_by= user, email="asdd@asdasd.com")
    company1.put()
    task1 = Task(title = "Name", create_by= user, company = company1)
    task1.put()
    self.assertEqual(False, task1.is_done)
    
  def test_list_user_Task(self):
    user1 = User(email = "test1@foo.com")
    user2 = User(email = "test2@foo.com")
    company1 = Company(name = "Name", create_by= user1, email="asdd@asdasd.com")
    company1.put()
    task1 = Task(title = "Name", create_by= user1, atach_users = [user1, user2], company = company1)
    task1.put()

    self.assertEqual(1, len(Task.all().fetch(10)))
    self.assertEqual(2, len(Task.all().fetch(1)[0].atach_users))
    self.assertEqual(user1, Task.all().fetch(1)[0].atach_users[0])
    self.assertEqual(user2, Task.all().fetch(1)[0].atach_users[1])

  def test_find_task_company(self):
    user1 = User(email = "test1@foo.com")
    user2 = User(email = "test2@foo.com")
    company1 = Company(name = "Name", create_by= user1, email="asdd@asdasd.com")
    company1.put()
    company2 = Company(name = "Name", create_by= user1, email="asdd@asdasd.com")
    company2.put()
    task1 = Task(title = "Name", create_by= user1, atach_users = [user1, user2], company = company1)
    task1.put()
    task2 = Task(title = "Name2", create_by= user1, atach_users = [user1, user2], company = company1)
    task2.put()
    task3 = Task(title = "Name3", create_by= user1, atach_users = [user1, user2], company = company2)
    task3.put()
    task4 = Task(title = "Name4", create_by= user1, atach_users = [user1, user2], company = company2)
    task4.put()

    query = Task.all().filter("company = ", company1)
    self.assertEqual(2, len(query.fetch(20)))




