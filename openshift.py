#!/usr/bin/env python
import tornado.web

class MainHandler(tornado.web.RequestHandler):
     def get(self):
          self.render('index.html',title ='Tornado on Openshift')

# Put here yours handlers.

handlers = [(r'/',MainHandler), ]
