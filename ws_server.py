import tornado.escape
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.options
import logging
import uuid
from argparse import Namespace
import sample
import json
from tornado.options import define, options

define('port', default=2886, help="The tornado server port", type=int)

class WebSocketSever(tornado.websocket.WebSocketHandler):
    bao_cons = set()
    bao_waiters = {}
    global con_key

    def open(self):
        sole_id = str(uuid.uuid4()).upper()
        self.con_key = sole_id
        self.bao_waiters["{}".format(sole_id)] = self
        self.bao_cons.add(self)
        self.write_message({"websocket_sole_id": sole_id})
        logging.info("websocket opened!")
    def on_message(self, message):
        if message == "close":
            self.close()
            return
        try:
            messaged = json.loads(message)
            args = Namespace(n=messaged['num'], prime=messaged['first'], sample=messaged['sample'], save_dir='save/'+messaged['type'])
            apple = sample.sample(args)
            tensor_data = apple.decode()
            data = {"tensor_data": tensor_data,"websocket_sole_id": self.con_key}
            self.write_message(data)
        except Exception as e:
            logging.info(e)

    def check_origin(self, origin: str):
        return True

    def allow_draft76(self):
        return True

    def on_close(self):
        self.bao_cons.remove(self)
        self.bao_waiters.pop(self.con_key)
        logging.info("websocket closed!")

class Application(tornado.web.Application):
    def __init__(self, handlers, setting):
        super(Application, self).__init__(handlers, **setting)


def main():
    options.parse_command_line()
    handlers = [(r"/", WebSocketSever)]
    setting = dict(xsrf_cookies=False)
    app = Application(handlers, setting)
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()