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
    task1 = Task(title = "Name", create_by= user)
    task1.put()
    task2 = Task(title = "Name", create_by= user)
    task2.put()

    self.assertEqual(2, len(Task.all().fetch(2)))

  def test_without_name_Task(self):  
    user = User(email = "test@foo.com")
    self.assertRaises(db.BadValueError, Task, create_by= user)

  def test_without_user_Task(self):  
    self.assertRaises(db.BadValueError, Task, title= "asdasd")

  def test_default_id_done_Task(self):  
    user = User(email = "test@foo.com")
    task1 = Task(title = "Name", create_by= user)
    task1.put()
    self.assertEqual(False, task1.is_done)

