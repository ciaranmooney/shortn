#! /usr/bin/env python

import web
from web import form

import hashlib
import time

temp = 30 # Number of seconds to keep temporary URLs

render = web.template.render("templates/")

urls = ( "/(.*)", "index")

app = web.application(urls, globals())
 
database = {}

myform = form.Form(
    form.Textbox("URL", form.notnull),
    form.Checkbox("Temporary?", value='something')
    )

class index:
    def GET(self, name):
        print name
        
        if name in database.keys(): 
            return web.seeother(database[name])
        else:
            form = myform()
            return render.formtest(form)

    def POST(self, unknown):
        print unknown
        form = myform()
        if not form.validates():
            return render.formtest(form)

        else:
          timestamp = time.time()
          database[hashlib.sha224(form.d.URL).hexdigest()[:8]] = (form.d.URL,\
          form["Temporary?"].checked, timestamp)
          print form["Temporary?"].checked, form.d.URL
          return "Current Datbase", database

if __name__ == "__main__":
    web.internalerror = web.debugerror
    app.run()


