# -*- coding: utf-8 -*-
"""Create an application instance."""
from livereload import Server

import app.app as app

app = app.create_app()
# remember to use DEBUG mode for templates auto reload
# https://github.com/lepture/python-livereload/issues/144
app.debug = True

server = Server(app.wsgi_app)
# server.watch
server.serve()
