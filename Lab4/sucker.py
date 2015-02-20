import os
import re

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

def IsValidChecksum(number):
    numlist = [int(x) for x in reversed(str(number)) if x.isdigit()]
    count = sum(x for i, x in enumerate(numlist) if i % 2 == 0)
    count += sum(sum(divmod(2 * x, 10)) for i, x in enumerate(numlist) if i % 2 != 0)
    return (count % 10 == 0)

def IsValidCharacters(number):
    if re.compile('^[-0-9]*$').match(number):
        return True
    else:
        return re.compile('^([0-9]{4}[-])*([0-9]{4})$').match(number) != None

def IsValidPattern(number, type):
    CC_PATTERNS = {
    'mastercard':'^5[12345]([0-9]{14})$',
    'visa'      :'^4([0-9]{15})$',
    }
    return re.compile(CC_PATTERNS[type]).match(number) != None

def IsValid(number, type):
    if IsValidCharacters(number):
        clean = number.replace('-', '')
        if IsValidPattern(clean, type):
            return IsValidChecksum(clean)
    return False

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        error = self.get_argument('error', None)
        if error == 'incomplete':
            self.render('error.html', error_msg="You didn't fill the form completely.")
        elif error == 'wrongcard':
            self.render('error.html', error_msg="You didn't provide a valid card number.")
        else:
            self.render('buyagrade.html')

    def post(self):
    	name = self.get_argument('name', None)
        section = self.get_argument('section', None)
        card = self.get_argument('card', None)
        card_type = self.get_argument('card_type', None)

        if not name or not section or not card or not card_type:
        	self.redirect('/?error=incomplete')
        elif not IsValid(card, card_type):
            self.redirect('/?error=wrongcard')
        else:
            current = dict()
            current['name'] = name
            current['section'] = section
            current['card'] = card.replace('-', '')
            current['card_type'] = card_type

            f = open(os.path.join(os.path.dirname(__file__),
                                'static', 'suckers.txt'), 'r')
            suckers = [line.strip('\n') for line in f.readlines()]
            f.close()

            f = open(os.path.join(os.path.dirname(__file__),
                                'static', 'suckers.txt'), 'a')

            f.write(';'.join([name, section, card, card_type]) + "\n")
            f.close()
            self.render('sucker.html', name=name, section=section, id=card, type=card_type,records=suckers)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
            )
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()