import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on this port", type=int)

'''new a item'''
class item:
	def __init__(self, name, filetype, size):
		self.name = name
		self.filetype = filetype
		if size < 1024:
			self.size = "%d b" % size
		elif size < 1024 * 1024:
			size /= 1024
			self.size = "%d kb" % size
		else:
			size /= (1024*1024)
			self.size = "%d mb" % size

'''main handler'''
class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		playlist = self.get_argument('playlist', 'None')
		filepath = os.path.join(os.path.dirname(__file__), "static/songs")
		filenames = os.listdir(filepath)

		if playlist is not 'None':
			listfile = open(os.path.join(filepath, playlist))
			filenames = listfile.read().splitlines()

		files = []
		for filename in filenames:
			files.append(item(filename,
				              os.path.splitext(filename)[1][1:],
				              os.path.getsize(os.path.join(filepath, filename))))

		files.sort(key=lambda x: (x.filetype))
		self.render(
            'music.html',
            title="Music Viewer",
            h1="190M Music Playlist Viewer",
            h2="Search Through Your Playlists and Music",
            files=files
        )

def main():
	tornado.options.parse_command_line()
	app = tornado.web.Application(
		handlers=[(r'/', IndexHandler)],
		template_path=os.path.join(os.path.dirname(__file__), "template"),
		static_path=os.path.join(os.path.dirname(__file__), "static/songs"),
		debug=True
	)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	main()
