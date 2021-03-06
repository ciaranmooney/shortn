#! /usr/bin/env python

import web
from web import form

import hashlib
import time
# need to figure out a way of handling file commits. Having a flat file probably
# wont work for multiple uses, as it has to be written and closed in each loop.
# Will probably have to farm that out to a sub process too, or get conformation
# back that it's actually been commited, then finish?

temp = 30 # Number of seconds to keep temporary URLs

render = web.template.render("templates/")
links = open("links", "w")

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
            return web.seeother(database[name][0])
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
          lock = open("lock", "w") # should probably include a random number
          print(form["Temporary?"].checked, form.d.URL)
          line = "%(URL)s, %(check)s, %(time)f" % {"URL":form.d.URL, \
          "check":form["Temporary?"].checked, "time":timestamp}
          links.write(line)
          links.close()
          return "Current Datbase", database
          lock.close()

if __name__ == "__main__":
    web.internalerror = web.debugerror
    app.run()


