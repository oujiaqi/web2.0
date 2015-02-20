import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on this port", type=int)


'''get film info'''
class film:
	def __init__(self, name, year, review, number, view):
		if int(review) < 60:
			self.rel = "images/rottenbig.png"
		else:
			self.rel = "images/freshbig.png"
		self.name = name
		self.year = year
		self.review = review
		self.number = number
		self.view = view
		

'''comments'''
class comment:
	'''get movie comment'''
	def __init__(self, content, cla, name, origin):
		self.content = content
		self.cla = cla.capitalize()
		self.name = name
		self.origin = origin
		self.rel = "images/" + cla + ".gif"

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		movie = self.get_argument("movie", "tmnt")
		path = os.path.dirname(__file__)
		imgpath = os.path.join(path, "static/images")
		fpath = os.path.join(path, "static/moviefiles/" + movie)
		mov = getDirFilmMessage(fpath)
		com = getDirComment(fpath)
		num = len(com)
		num /= 2
		commentl = com[:num]
		commentr = com[num:]
		poster="moviefiles/" + movie + "/generaloverview.png"
		self.render("tmnt.html",
			movie=mov,
			commentl=commentl,
			commentr=commentr,
			poster=poster)




def getDirFilmMessage(path):
	try:
		fs = open(os.path.join(path,"info.txt"), 'r')
		info = fs.read().splitlines()
	finally:
		if fs:
			fs.close()
	view = []

	try:
		fs = open(os.path.join(path,"generaloverview.txt"), 'r')
		for one in fs.read().splitlines():
			view.append(one.split(":"))
	finally:
		if fs:
			fs.close()

	return film(info[0], info[1], info[2], info[3], view)


def getDirComment(path):
	allComment = []
	fileList = os.listdir(path)
	for oneFile in fileList:
		if oneFile.find("review") != -1:
			fs = open(os.path.join(path,oneFile), 'r')
			re = fs.read().splitlines()
			co = comment(re[0], re[1].lower(), re[2], re[3])
			allComment.append(co)
			fs.close()

	return allComment

if __name__ == "__main__":
	tornado.options.parse_command_line()
	app = tornado.web.Application(
		handlers=[(r'/', IndexHandler)],
		template_path=os.path.join(os.path.dirname(__file__), "template"),
		static_path=os.path.join(os.path.dirname(__file__), "static"),
		debug=True,
		autoescape=None
	)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()