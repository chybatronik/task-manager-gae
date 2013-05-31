from splinter import Browser
import unittest
from google.appengine.ext import db
from google.appengine.api.users import User
from google.appengine.ext import testbed
from google.appengine.datastore import datastore_stub_util

from main import *

class LoginTestCase(unittest.TestCase):

  def setUp(self):
    self.testbed = testbed.Testbed()
    self.testbed.activate()
    self.testbed.init_datastore_v3_stub()
    self.testbed.init_memcache_stub()
    self.browser = Browser()

  def tearDown(self):
    self.testbed.deactivate()

  def test_login(self):
    self.browser.visit("http://127.0.0.1:8080/")
    self.assertEqual(self.browser.find_by_tag("h3").first.text, "Not logged in")

    self.browser.find_by_id("submit-login").first.click()
    self.assertEqual(self.browser.find_link_by_text("Insurance").first.text, "Insurance")

  def test_logout(self):
    self.browser.visit("http://127.0.0.1:8080/")
    self.assertEqual(self.browser.find_by_tag("h3").first.text, "Not logged in")

    self.browser.find_by_id("submit-login").first.click()
    self.assertEqual(self.browser.find_link_by_text("Insurance").first.text, "Insurance")

    self.browser.find_link_by_text("Log out").first.click()
    self.assertEqual(self.browser.find_by_tag("h3").first.text, "Not logged in")


