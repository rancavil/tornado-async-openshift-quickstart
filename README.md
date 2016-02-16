Tornado Web Server and Python 3 on Openshift
============================================

This git repository helps you get up and run quickly Tornado Web Server on Openshift. 

Running on Openshift
--------------------

Create an account at http://openshift.redhat.com/

Install the RHC client tools if you have not already done so:

     sudo gem install rhc

Create a python-3.3 application

     rhc app create tornadopy3 python-3.3

Add this upstream repo

     cd tornadopy3
     git remote add upstream -m master git://github.com/rancavil/tornado-async-openshift-quickstart.git
     git pull -s recursive -X theirs upstream master

Then push the repo upstream

     git push

That's it. You can now checkout your application at:

     http://tornadopy3-$youtnamespace.rhcloud.com

The structure of directories created are:

     tornadopy3/
          wsgi.py.disable
          .gitignore
          README.md
          setup.py
          requirements.txt
          openshift.py
          app.py
          .openshift/
               action_hooks/
               cron/
               markers/
          static/
               README
          templates/
               index.html

The main file is openshift.py, this contains the definitions of the handlers. You can change it the name, but you must be sure to change the import statement in app.py file.

     import tornado.web
     import os

     class MainHandler(tornado.web.RequestHandler):
          def get(self):
               self.render('index.html')

     # Put here yours handlers.

     handlers = [(r'/',MainHandler),]

Openshift uses app.py to deploy the python applications. In the app.py file we will define.

     port = int(os.environ.get('OPENSHIFT_PYTHON_PORT', '8000'))
     ip = os.environ.get('OPENSHIFT_PYTHON_IP', 'localhost')

     if __name__ == '__main__':
          application = tornado.web.Application(handlers, **settings)
          application.listen(port, ip)
          tornado.ioloop.IOLoop.instance().start()

app.py will be used by Openshift to execute the server.
