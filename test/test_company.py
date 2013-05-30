import unittest
from google.appengine.ext import db
from google.appengine.api.users import User
from google.appengine.ext import testbed
from google.appengine.datastore import datastore_stub_util

from main import *
from datetime import datetime

class CompanyTestCase(unittest.TestCase):

  def setUp(self):
    self.testbed = testbed.Testbed()
    self.testbed.activate()
    self.testbed.init_datastore_v3_stub()
    self.testbed.init_memcache_stub()

  def tearDown(self):
    self.testbed.deactivate()

  def testCompany(self):
    user = User(email = "test@foo.com")
    company1 = Company(name = "Name", create_by= user, email="asdd@asdasd.com")
    company1.put()
    company2 = Company(name = "Name", create_by= user, email="asdd@asdasd.com")
    company2.put()

    self.assertEqual(2, len(Company.all().fetch(2)))

  def test_without_name_Company(self):  
    user = User(email = "test@foo.com")
    self.assertRaises(db.BadValueError, Company, create_by= user, email="asdd@asdasd.com")

  def test_without_user_Company(self):    
    self.assertRaises(db.BadValueError, Company, name="asd", email="asdd@asdasd.com")

  def test_with_user_Company(self):
    user = User(email = "test@foo.com")
    Company(name = "qwe", create_by= user, email="asdd@asdasd.com").put()

    self.assertEqual(1, len(Company.all().fetch(2)))

  def test_datetime_Company(self):
    user = User(email = "test@foo.com")
    Company(name = "qwe", create_by= user, email="asdd@asdasd.com").put()
    self.assertTrue(Company.date)
    
  def test_without_email_Company(self):  
    user = User(email = "test@foo.com")
    self.assertRaises(db.BadValueError, Company, name= "asdasd", create_by= user)


if __name__ == '__main__':
    unittest.main()