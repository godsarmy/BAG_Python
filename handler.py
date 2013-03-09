import webapp2
import json
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)+"/template"))

class AjaxHandler(webapp2.RequestHandler):
    data = {
        "index":[
            { "url" : "/",             "name" : "Index" },
            { "url" : "hero",          "name" : "Hero" },
            { "url" : "fluid",         "name" : "Fluid" },
            { "url" : "signin",        "name" : "Sign In" },
            { "url" : "sticky-footer", "name" : "Sticky-Footer" },
            { "url" : "sfn",           "name" : "Sticky-Footer Navbar" },
            { "url" : "justified-nav", "name" : "Justified Navbar" },
            { "url" : "carousel",      "name" : "Carousel" },
            { "url" : "market-narrow", "name" : "Market Narrow" },
            { "url" : "static-grid",   "name" : "Static Grid" },
            { "url" : "ajax-grid",     "name" : "Ajax Grid" },
            { "url" : "angular-ui",    "name" : "Angular UI" },
        ],
        "grid": {
            "head": [
                {"key":"name", "desc":"Name"},
                {"key":"creator", "desc":"Creator"},
                {"key":"engine", "desc":"Engine"},
                {"key":"license", "desc":"Software License"},
            ],
            "body": [
                {"name":"Chrome",  "creator":"Google", "engine":"Webkit", "license":"BSD"},
                {"name":"Firefox", "creator":"Mozilla", "engine":"Gecko", "license":"MPL/GPL/LGPL"},
                {"name":"Internet Explorer", "creator":"Microsoft", "engine":"Trident", "license":"Proprietary"},
            ]
        },
    } 

    def get(self):
        call_type = self.request.get('type')
        content = self.request.get('content')

        data = {}
        if (content == 'detail'):
            data = { 
                 "detail" : ("This is %s detail inform generated via Ajax call by AngularJS." % call_type )
                 }
        else:
            data = self.data[call_type]
        self.response.out.write(json.dumps(data))

class AngularUIHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
                'project_name': "BAG Python",
                'moduleName': "myApp",
        }

        template = jinja_environment.get_template('angular-ui.tpl')
        self.response.out.write(template.render(template_values))

class AjaxGridHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
                'project_name': "BAG Python",
        }

        template = jinja_environment.get_template('ajax-grid.tpl')
        self.response.out.write(template.render(template_values))

class StaticGridHandler(webapp2.RequestHandler):
    data = [
             {"name":"Chrome",  "creator":"Google", "engine":"Webkit", "license":"BSD"},
             {"name":"Firefox", "creator":"Mozilla", "engine":"Gecko", "license":"MPL/GPL/LGPL"},
             {"name":"Internet Explorer", "creator":"Microsoft", "engine":"Trident", "license":"Proprietary"},
    ]

    def get(self):
        template_values = {
                'project_name': "BAG Python",
                "data": self.data
        }

        template = jinja_environment.get_template('grid.tpl')
        self.response.out.write(template.render(template_values))

class MarketNarrowHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
                'project_name': "BAG Python"
        }
        template = jinja_environment.get_template('market-narrow.tpl')
        self.response.out.write(template.render(template_values))

class CarouselHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
                'project_name': "BAG Python"
        }
        template = jinja_environment.get_template('carousel.tpl')
        self.response.out.write(template.render(template_values))

class StickyFooterHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
                'project_name': "BAG Python"
        }

        template = jinja_environment.get_template('sticky-footer.tpl')
        self.response.out.write(template.render(template_values))

class StickyFooterNavHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
                'project_name': "BAG Python"
        }

        template = jinja_environment.get_template('sfn.tpl')
        self.response.out.write(template.render(template_values))

class JustifiedNavHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
                'project_name': "BAG Python"
        }

        template = jinja_environment.get_template('justified-nav.tpl')
        self.response.out.write(template.render(template_values))

class SigninHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
                'project_name': "BAG Python"
        }

        template = jinja_environment.get_template('signin.tpl')
        self.response.out.write(template.render(template_values))

class HeroHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
                'project_name': "BAG Python",
        }

        template = jinja_environment.get_template('hero.tpl')
        self.response.out.write(template.render(template_values))

class FluidHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
                'project_name': "BAG Python",
                'username': "Unknown",
        }

        template = jinja_environment.get_template('fluid.tpl')
        self.response.out.write(template.render(template_values))

    def post(self):
        username = self.request.get('address') or 'Unknown'
        template_values = {
                'project_name': "BAG Python",
                'username': username,
        }

        template = jinja_environment.get_template('fluid.tpl')
        self.response.out.write(template.render(template_values))

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
                'project_name': "BAG Python"
        }

        template = jinja_environment.get_template('index.tpl')
        self.response.out.write(template.render(template_values))


