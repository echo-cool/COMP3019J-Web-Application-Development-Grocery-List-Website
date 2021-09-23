# -*- coding: utf-8 -*-
"""Create an application instance."""
from livereload import Server

import project.app as app
from project import settings

app = app.create_app()
# remember to use DEBUG mode for templates auto reload
# https://github.com/lepture/python-livereload/issues/144
# if settings.DEBUG:
#     server = Server(project.wsgi_app)
#     server.serve()
# server.watch

