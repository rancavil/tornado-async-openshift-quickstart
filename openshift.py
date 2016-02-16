#!/usr/bin/env python
import tornado.web

from datetime import datetime

class BaseHandler(tornado.web.RequestHandler):
     def set_default_headers(self):
          self.set_header("Access-Control-Allow-Origin", "*")
          self.set_header("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
          self.set_header("Access-Control-Allow-Headers","Content-Type, Depth, User-Agent, X-File-Size, X-Requested-With, X-Requested-By, If-Modified-Since, X-File-Name, Cache-Control")

class MainHandler(BaseHandler):
     def get(self):
          self.render('index.html',title ='Tornado on Openshift')

class PersonService(BaseHandler):
     def get(self):
          self.set_header('Content-Type','application/json')
          self.write('{"first_name" : "Rodrigo","middle_name": "Andres", "last_name" : "Ancavil","timestamp" :"'+str(datetime.now())+'"}')


# Put here yours handlers.

handlers = [(r'/',MainHandler), (r'/person',PersonService),]
