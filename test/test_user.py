from splinter import Browser
import unittest
from google.appengine.ext import db
from google.appengine.api.users import User
from google.appengine.ext import testbed
from google.appengine.datastore import datastore_stub_util

from main import *

class UserTestCase(unittest.TestCase):

  def setUp(self):
    self.testbed = testbed.Testbed()
    self.testbed.activate()
    self.testbed.init_datastore_v3_stub()
    self.testbed.init_memcache_stub()
    #self.browser = Browser('chrome')

  def tearDown(self):
    self.testbed.deactivate()

  def test_avatar(self):
    user = User(email = "test@foo.com")
    user_insurance = UserInsurance(user=user)
    user_insurance.put()
    self.assertFalse(user_insurance.avatar)
    self.assertEqual(1, len(UserInsurance.all().fetch(5)))