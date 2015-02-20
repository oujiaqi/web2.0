#-*-encoding:utf8-*-

import os.path
import re

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import sys 
reload(sys) 
sys.setdefaultencoding('utf8') 

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)



'''question'''
class QUESTION(object):
    def __init__(self,Good,Answer,Type,View,Name,Time,Question,Label):
        self.Good = Good
        self.Answer = Answer
        self.Type = Type
        self.View = View
        self.Name = Name
        self.Time = Time
        self.Question = Question
        self.Label =Label



'''User'''
class USER(object):
    def __init__(self,name,password):
        self.name = name
        self.password = password



'''get all users info'''
def getAllUsers():
    fpath = os.path.dirname(__file__)
    spath = os.path.join(fpath, "static")
    Upath = os.path.join(spath, "userData","users.txt")
    f = open(Upath,'r')
    users = []
    for one in f.readlines():
        msg = one.strip('\n').split(',')
        user = USER(msg[0], msg[1])
        users.append(user)
    f.close()
    return users



'''get all qusetions'''
def getAllQuestions():
    fpath = os.path.dirname(__file__)
    spath = os.path.join(fpath, "static")
    dpath = os.path.join(spath,"questionData")
    qpath = os.path.join(dpath, "questions.txt")
    f = open(qpath,'r')
    questions = []
    for line in f.readlines():
        m = line.strip('\n').split(";")
        qu = QUESTION(m[0],m[1],m[2],m[3],m[4],m[5],m[6],m[7])
        questions.append(qu)
    f.close()
    return questions



'''write user'''
def writeNewUser(new):
    fpath = os.path.dirname(__file__)
    spath = os.path.join(fpath, "static")
    Upath = os.path.join(spath, "userData","users.txt")
    f = open(Upath,'a')
    f.write(new.name + "," + new.password + "\n")
    f.close()



'''write question'''
def writeQuestion(q):
    fpath = os.path.dirname(__file__)
    spath = os.path.join(fpath, "static")
    dpath = os.path.join(spath,"questionData")
    qpath = os.path.join(dpath, "questions.txt")
    f = open(qpath,'a')
    f.write(q.Good + ";" + q.Answer + ";" + q.Type + ";" + q.View + ";" + q.Name + ";" + q.Time + ";" + q.Question + ";" + q.Label + "\n")



'''match user'''
def match(user):
    Users = getAllUsers()
    for one in Users:
        if one.name == user.name and one.password == user.password:
            return True
    return False



'''valid signup name'''
def isValidName(New):
    Users = getAllUsers()
    for one in Users:
        if one.name == New.name:
            return False
    if re.compile("\w+").match(New.name) != None:
        if re.compile("\w{6,20}").match(New.password) != None:
            return True;
    return False


'''base handler'''
class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")



'''index handler'''
class IndexHandler(BaseHandler):
    def get(self):
        questions = getAllQuestions()
        name = self.get_secure_cookie("user")
        self.render("index.html", questions = questions, name = name)


'''login handler'''
class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html", error_msg = None)

    def post(self):
        name = self.get_argument("name", None)
        password = self.get_argument("password", None)
        test = USER(name, password)
        if match(test):
            self.set_secure_cookie("user", name)
            self.redirect("/")
        else:
            error_msg = "Invalid Input!"
            self.render("login.html", error_msg = error_msg)


'''ask handler'''
class AskHandler(BaseHandler):
    def get(self):
        title = "Ask"
        name = self.get_secure_cookie("user")
        self.render("ask.html", title=title, name=name)

    def post(self):
        title = self.get_argument("title", "None").replace(";", "|")
        tags = self.get_argument("tags", "None").replace(";", "|")
        content = self.get_argument("content", "None").replace(";", "|")
        main = title + "  " + content
        name = self.get_secure_cookie("user")
        if name:
            q = QUESTION("0","0","回答","0",name,"1 mins ago",main,tags)
            writeQuestion(q)
            self.redirect("/")
        else:
            self.redirect("/login")



'''signup handler'''
class SignupHandler(BaseHandler):
    def get(self):
        self.render("signinup.html", error_msg = None)

    def post(self):
        name = self.get_argument("name", None)
        password = self.get_argument("password", None)
        new = USER(name, password)
        if isValidName(new):
            writeNewUser(new)
            self.set_secure_cookie("user", name)
            self.redirect("/")
        else:
            self.render("signinup.html", error_msg ="Your input is not valid")


'''log out'''
class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect("/")




if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r"/", IndexHandler),(r"/signup", SignupHandler),(r"/login", LoginHandler),(r"/ask",AskHandler),(r"/logout",LogoutHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True,
        cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo="
        )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()