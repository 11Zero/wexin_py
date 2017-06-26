# # -*- coding: utf-8 -*-
# # filename: main.py
# import web
#
# urls = (
#     '/app', 'Handle',
# )
#
#
# class Handle(object):
#     def GET(self):
#         return "hello, this is a test"
#
#
# if __name__ == '__main__':
#     app = web.application(urls, globals())
#     app.run()

from flask import Flask
# from redis import Redis, RedisError
import os
import socket

# Connect to Redis
# redis = Redis(host=os.environ.get('REDIS_PORT_6379_TCP_ADDR'), db=0, password=os.environ.get('REDIS_ENV_REDIS_PASS'))

app = Flask(__name__)


@app.route("/")
def hello():
    html = "<h3>tht {name}!</h3>" \
           "<b>myname:</b> {hostname}<br/>"
    return html.format(name=os.getenv('NAME', "world"), hostname=socket.gethostname())

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
