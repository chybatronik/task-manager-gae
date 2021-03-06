from re import match, IGNORECASE, UNICODE, VERBOSE
from google.appengine.ext import db
from google.appengine.api.users import User
from google.appengine.ext import blobstore
from google.appengine.api.images import get_serving_url
import urllib

class Category(db.Model):
    name = db.StringProperty(required=True)
    date = db.DateTimeProperty(auto_now_add=True)
    attach_users = db.ListProperty(User)
    create_by = db.UserProperty(required=True)


class Task(db.Model):
    title = db.StringProperty(required=True)
    text = db.TextProperty()
    is_done = db.BooleanProperty(default=False)
    attach_users = db.ListProperty(User)
    attach_files = db.ListProperty(blobstore.BlobKey)
    priority = db.RatingProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    create_by = db.UserProperty(required=True)

    def lm_text(self):
        if len(self.text) > 120:
            begin = self.text[0:120]
            end = self.text[120:-1]
            my_id = self.key().id()
            result = '''<div class="muted" style="margin-left:20px">''' + begin
            result += '''<a id="more_my_id" class="more" href=""> ... more  </a>
<div id="hidde_more_my_id" class="hidden"> '''.replace("my_id", str(my_id))
            result += end + '''<a id="less_more_my_id" class="less" href="">  less  </a></div></div>'''.replace("my_id", str(my_id))
            return result
        else:
            return self.text
    
    def get_urls_attach_files(self):
        result = []
        for key in self.attach_files:
            blob_info = blobstore.BlobInfo.get(key)
            filename =  blob_info.filename
            extensionsToCheck = ('.png', '.jpeg', '.jpg')
            if filename.lower().endswith(extensionsToCheck):
                image_url_200 = get_serving_url(key, 200)
                image_url_40 = get_serving_url(key, 40)
                image_url = get_serving_url(key, 1200)
            else:
                image_url = None
                image_url_200 = None
                image_url_40 = None

            return self.text
            di = {
                "image_url_200":image_url_200,
                "image_url_40":image_url_40,
                "image_url":image_url,
                "filename":filename,
                "key":str(key),
                "link_file":"/server?key="+str(key),
                "delete_url":'/uploads?key=' + str(key)
            }

            result.append(di)
        return result

class UserInsurance(db.Model):
    user = db.UserProperty(required=True)
    avatar = db.BlobProperty()

    def get_avatar(self):
        return "URL"
