#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import jinja2
import webapp2

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
JINJA_ENV = jinja2.Environment(
    loader = jinja2.FileSystemLoader(TEMPLATE_DIR),
    autoescape = True)

URLS = {
    'home' : '/'
}

TEMPLATES = {
    'home' : 'home.html'
}

def render_str(template, **params):
    t = JINJA_ENV.get_template(template)
    return t.render(params)

class OutputHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        return render_str(template, **params)

    def render(self, template, **kw):
        kw['urls'] = URLS
        print (kw)
        self.write(self.render_str(template, **kw))

    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)

class HomeHandler(OutputHandler):
    def get(self):
        self.render(TEMPLATES['home'])

app = webapp2.WSGIApplication(
[
    (URLS['home'], HomeHandler)
], debug=True)
