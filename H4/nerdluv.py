#-*-encoding:utf8-*-

'''set default encoding'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os.path
import re

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

def isComplete(name, gender, age, Type, Os, sex, minage, maxage):
    if name and gender and age and Type and Os and sex and minage and maxage:
        return True
    else:
        return False

class person:
    def __init__(self,name,gender,age,Type,Os,sex,minage,maxage):
        self.name = name
        self.age = age
        self.gender = gender
        self.Type = Type
        self.Os = Os
        self.sex = sex
        self.minage = minage
        self.maxage = maxage
        self.rating = -1
        TempName = name.lower().replace(" ", "_")
        fpath = os.path.dirname(__file__)
        spath = os.path.join(fpath, "static")
        ppath = os.path.join(spath, "images")
        if os.path.exists(os.path.join(ppath, TempName+".jpg")):
            self.picture = TempName+".jpg"
        else:
            self.picture = "default_user.jpg"
    def set_rating(self, num):
        self.rating = num


def isValid(age, Type, minage, maxage):
    if re.compile("[0-9]{1,2}").match(age) != None:
        if re.compile("(I|E)(N|S)(F|T)(J|P)").match(Type) != None:
            if re.compile("[0-9]{1,2}").match(minage) != None:
                if re.compile("[0-9]{1,2}").match(maxage) != None:
                    if int(minage) <= int(maxage):
                        return True
    return False

def match_rating(user, test):
    rating = -1
    if user.gender not in test.sex or test.gender not in user.sex:
        return rating;
    else:
        if int(test.minage) <= int(user.age) <= int(test.maxage) and int(user.minage) <= int(test.age) <= int(user.maxage):
            rating += 1
        if user.Os == test.Os:
            rating += 2
        for i in range(0, 4):
            if test.Type[i] == user.Type[i]:
                rating += 1
        return rating


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class MatchHandler(tornado.web.RequestHandler):
    def post(self):
        fpath = os.path.dirname(__file__)
        spath = os.path.join(fpath, "static")
        ppath = os.path.join(spath, "images")
        dpath = os.path.join(spath, "data")

        Name = self.get_argument("name", None)
        Gender = self.get_argument("gender", None)
        Age = self.get_argument("age", None)
        Type = self.get_argument("type", None)
        Os = self.get_argument("Os", None)
        Male = self.get_argument("male", "")
        Female = self.get_argument("female", "")
        Minage = self.get_argument("min_age", None)
        Maxage = self.get_argument("max_age", None)
        Sex = Male + Female

        succeed = True
        if not isComplete(Name, Gender, Age, Type, Os, Sex, Minage, Maxage):
            succeed = False
            error_message = "Sorry, your input is incomplete!"
            self.render("results.html",succeed = succeed,error_message = error_message)
        elif not isValid(Age, Type, Minage, Maxage):
            succeed = False
            error_message ="Sorry, your input is not valid!"
            self.render("results.html",succeed = succeed,error_message = error_message)

        persons = []
        if succeed:
            f = open(os.path.join(dpath, "singles.txt"), 'r')
            user = person(Name, Gender, Age, Type, Os, Sex, Minage, Maxage)
            for line in f.readlines():
                data = line.strip('\n').split(",")
                pe = person(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
                rating = match_rating(user, pe)
                if int(rating) >= 0:
                    pe.set_rating(int(rating))
                    persons.append(pe)
            f.close()

            f = open(os.path.join(dpath, "singles.txt"), 'a')
            f.write(Name + "," + Gender + "," + Age + "," + Type + "," + Os + "," + Sex + "," + Minage + "," + Maxage + "\n")
            f.close()

            file_name = Name.lower().replace(" ", "_") + ".jpg"
            upload_file = os.path.join(os.path.dirname(__file__), "static", "images", file_name)
            if 'file' in self.request.files:
                pic = self.request.files['file'][0]
                with open(upload_file,'wb') as up:
                    up.write(pic['body'])

            self.render("results.html",persons = persons,user = user,succeed=succeed)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler), (r'/result',MatchHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True
        )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
