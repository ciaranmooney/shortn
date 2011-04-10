#! /usr/bin/env python

import web

render = web.template.render("templates/")
urls = ( "/(.*)", "index")

app = web.application(urls, globals())

class index:
    def GET(self, name):
        return render.index(name)

if __name__ == "__main__":
    app.run()


