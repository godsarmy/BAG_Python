#model module to provide ajax inform
#
from google.appengine.ext import db

class Browser(db.Model):
    """Models an individual browser entry with an name, creator, engine and license"""
    creator = db.StringProperty()
    engine = db.StringProperty()
    license = db.StringProperty()

    @property
    def name(self):
        return self.key().name()

def get_browsers():
    browsers = db.GqlQuery("SELECT * FROM Browser")

    #build browser into
    body = []
    head = [
                {"key":"name", "desc":"Name"},
                {"key":"creator", "desc":"Creator"},
                {"key":"engine", "desc":"Engine"},
                {"key":"license", "desc":"Software License"},
           ]
    for browser in browsers:
        body.append({"name": browser.name, "creator": browser.creator,
                     "engine": browser.engine, "license": browser.license})

    return {"head": head, "body": body}

def init_browsers():

    browsers_info = [
                {"name":"Chrome",  "creator":"Google", "engine":"Webkit", "license":"BSD"},
                {"name":"Firefox", "creator":"Mozilla", "engine":"Gecko", "license":"MPL/GPL/LGPL"},
                {"name":"Internet Explorer", "creator":"Microsoft", "engine":"Trident", "license":"Proprietary"},
            ]

    for browser_info in browsers_info:
        browser = Browser(key_name=browser_info["name"])
        browser.creator = browser_info["creator"]
        browser.engine = browser_info["engine"]
        browser.license = browser_info["license"]
        browser.save()


