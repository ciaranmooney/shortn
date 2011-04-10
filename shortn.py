#! /usr/bin/env python

import web
from web import form

render = web.template.render("templates/")
urls = ( "/", "index")

app = web.application(urls, globals())

database = {}

myform = form.Form(
    form.Textbox("URL", form.notnull),
    form.Checkbox("Temporary?")
    )

class index:
    def GET(self):
        form = myform()
        return render.formtest(form)

    def POST(self):
        form = myform()
        if not form.validates():
            return render.formtest(form)

        else:
          return "Greeet"

if __name__ == "__main__":
    web.internalerror = web.debugerror
    app.run()


