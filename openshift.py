#!/usr/bin/env python
import tornado.web

class MainHandler(BaseHandler):
     def get(self):
          self.render('index.html',title ='Tornado on Openshift')

# Put here yours handlers.

handlers = [(r'/',MainHandler), ]
