# The purpose of this file is to deal with the issue of sending email
from threading import Thread

# import mail
from flask import current_app, render_template
# import smtplib
# from . import mail

#
# def send_async_email(app, msg):
#     return 0
#     # with app.app_context():
#     #     mail.send(msg)
#
#
# def send_email(to, subject, template, **kwargs):
#     app = current_app._get_current_object()
#     msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
#                   sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
#     msg.body = render_template(template + '.txt', **kwargs)
#     msg.html = render_template(template + '.html', **kwargs)
#     thr = Thread(target=send_async_email, args=[app, msg])
#     thr.start()
#     return thr


