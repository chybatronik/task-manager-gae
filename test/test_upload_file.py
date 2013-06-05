from splinter import Browser
import unittest
from google.appengine.ext import db
from google.appengine.api.users import User
from google.appengine.ext import testbed
from google.appengine.datastore import datastore_stub_util
from time import sleep
from main import *

class UploadTestCase(unittest.TestCase):

  def setUp(self):
    self.testbed = testbed.Testbed()
    self.testbed.activate()
    self.testbed.init_datastore_v3_stub()
    self.testbed.init_memcache_stub()
    self.browser = Browser('chrome')

  def tearDown(self):
    self.testbed.deactivate()

  def test_when_create_task_upload_file(self):
    #login
    self.browser.visit("http://127.0.0.1:8080/")
    self.assertEqual(self.browser.find_by_tag("h3").first.text, "Not logged in")
    self.browser.find_by_id("submit-login").first.click()
    self.assertEqual(self.browser.find_link_by_text("Insurance").first.text, "Insurance")

    self.browser.visit("http://127.0.0.1:8080/tasks")

    self.browser.click_link_by_text('Create new task')

    self.browser.fill('title', 'title')
    self.browser.fill('text', 'text')

    self.browser.is_element_present_by_name('files[]', wait_time=10)

    self.browser.attach_file('files[]', os.path.join(os.path.dirname(__file__),'1.png'))
    #self.browser.attach_file('files[]', 'test/1.png')
    self.browser.find_by_css('.btn.btn-primary.start').first.click()


    self.assertEqual(1, len(self.browser.find_by_css('.template-download.fade.in')))
    self.assertEqual(4, len(self.browser.find_by_css('.template-download.fade.in td')))

  def test_when_create_task_upload_many_files(self):
    #login
    self.browser.visit("http://127.0.0.1:8080/")
    self.assertEqual(self.browser.find_by_tag("h3").first.text, "Not logged in")
    self.browser.find_by_id("submit-login").first.click()
    self.assertEqual(self.browser.find_link_by_text("Insurance").first.text, "Insurance")

    self.browser.visit("http://127.0.0.1:8080/tasks")

    self.browser.click_link_by_text('Create new task')

    self.browser.fill('title', 'title')
    self.browser.fill('text', 'text')

    self.browser.is_element_present_by_name('files[]')

    self.browser.attach_file('files[]', os.path.join(os.path.dirname(__file__),'1.png'))
    self.browser.attach_file('files[]', os.path.join(os.path.dirname(__file__),'1.png'))
    self.browser.attach_file('files[]', os.path.join(os.path.dirname(__file__),'1.png'))

    #self.browser.attach_file('files[]', 'test/1.png')
    self.browser.find_by_css('.btn.btn-primary.start').first.click()
    sleep(3)

    self.assertEqual(3, len(self.browser.find_by_css('.files tr.template-download')))
    #self.assertEqual(4, len(self.browser.find_by_css('.template-download.fade.in td')))


