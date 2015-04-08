#-*-encoding:utf8-*-

import os.path
import re
import time
import random

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import sys 
reload(sys) 
sys.setdefaultencoding('utf8')

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


NAME = ["六道仙人","十尾","人柱力","漩涡鸣人","春野樱","日向雏田","日向宁次","李洛克","天天","犬冢牙","油女志乃","奈良鹿丸","秋道丁次","山中井野","宇智波佐助","佩恩","长门","小南","宇智波鼬","干柿鬼鲛","迪达拉","赤砂之蝎","阿飞","宇智波斑","角都","卡卡西","飞段","大蛇丸","宇智波斑","自来也","纲手","桃地再不斩","干柿鬼鲛","黑锄雷牙","鬼灯满月","君麻吕","鬼童丸","多由也","宇智波带土","宇智波泉奈","千手柱间","千手扉间","猿飞日斩","猿飞阿斯玛","鬼灯水月","天秤重吾","香磷","团藏","佐井","我爱罗","水影"]

'''Article'''
class ARTICLE(object):
    def __init__(self, Title, Stitle, Sdate, Rdate, Comment, Love, Content, Visit):
        self.Title = Title
        self.Stitle = Stitle
        self.Sdate = Sdate
        self.Rdate = Rdate
        self.Comment = Comment
        self.Love = Love
        self.Content = Content
        self.Visit = Visit


'''Comment'''
class COMMENT(object):
    def __init__(self, Name, Picture, Class, Date, Content):
        self.Name = Name
        self.Picture = Picture
        self.Class = Class
        self.Date = Date
        self.Content = Content


'''get all visit'''
def getAllVisit():
    fpath = os.path.join(os.path.dirname(__file__), "static", "main.txt")
    f = open(fpath, 'r')
    visit = []
    for one in f.readlines():
        one = one.strip()
        visit.append(one)
    f.close()
    return visit


'''get article content in P'''
def getContent(visit):
    fpath = os.path.join(os.path.dirname(__file__), "static", "articles", visit + ".txt")
    f = open(fpath, 'r')
    content = []
    for one in f.readlines():
        content.append(one)
    f.close()
    return content


'''get article info'''
def getInfo(visit):
    fpath = os.path.join(os.path.dirname(__file__), "static", "info", visit + ".txt")
    f = open(fpath, 'r')
    info = []
    for one in f.readlines():
        info.append(one.strip("\n"))
    f.close()
    return info

'''get one article'''
def getOneArticle(visit):
    content = getContent(visit)
    info = getInfo(visit)
    return ARTICLE(info[1], info[2], info[0], info[3], info[4], info[5], content, visit)



'''get all articles'''
def getAllArticles():
    visits = getAllVisit()
    articles = []
    for visit in visits:
        article = getOneArticle(visit)
        articles.append(article)
    return articles


'''get all comments'''
def getAllComments(visit):
    fpath = os.path.join(os.path.dirname(__file__), "static", "comments", visit + ".txt")
    f = open(fpath, 'r')
    comments = []
    for one in f.readlines():
        one = one.strip().split(';')
        if len(one) > 4:
            content = one[4].replace("^", "\n")
            comment = COMMENT(one[0], one[1], one[2], one[3], content)
            comments.append(comment)
    return comments


'''get all message'''
def getAllMessage():
    fpath = os.path.join(os.path.dirname(__file__), "static", "message", "message.txt")
    f = open(fpath, 'r')
    comments = []
    for one in f.readlines():
        one = one.strip().split(";")
        if len(one) > 4:
            content = one[4].replace("^", "\n")
            comment = COMMENT(one[0], one[1], one[2], one[3], content)
            comments.append(comment)
    return comments


'''get all impression'''
def getAllImpression():
    fpath = os.path.join(os.path.dirname(__file__), "static", "message", "impression.txt")
    f = open(fpath, 'r')
    message = []
    for one in f.readlines():
        one = one.strip()
        message.append(one)
    return message


'''add one love number'''
def addOneLoveNum(visit):
    info = getInfo(visit)
    love = str(int(info[5]) + 1)
    fpath = os.path.join(os.path.dirname(__file__), "static", "info", visit + ".txt")
    f = open(fpath, 'w')
    f.write(info[0] + '\n' + info[1] + '\n' + info[2] + '\n' + info[3] + '\n' + info[4] + '\n' + love)
    f.close()


'''add one comment number'''
def addOneCommentNum(visit):
    info = getInfo(visit)
    comment = str(int(info[4]) + 1)
    fpath = os.path.join(os.path.dirname(__file__), "static", "info", visit + ".txt")
    f = open(fpath, 'w')
    f.write(info[0] + '\n' + info[1] + '\n' + info[2] + '\n' + info[3] + '\n' + comment + '\n' + info[5])
    f.close()


'''add one comment'''
def addOneComment(visit, comment):
    fpath = os.path.join(os.path.dirname(__file__), "static", "comments", visit + ".txt")
    f = open(fpath, 'a')
    f.write(comment.Name + ';' + comment.Picture + ';' + comment.Class + ';' + comment.Date + ';' + comment.Content + "\n")
    f.close()


'''add one Message'''
def addOneMessage(comment):
    fpath = os.path.join(os.path.dirname(__file__), "static", "message", "message.txt")
    f = open(fpath, "a")
    f.write(comment.Name + ';' + comment.Picture + ';' + comment.Class + ';' + comment.Date + ';' + comment.Content + "\n")
    f.close()

'''add one Impression'''
def addOneImpression(impression):
    fpath = os.path.join(os.path.dirname(__file__), "static", "message", "impression.txt")
    impression = "\n".join(impression)
    f = open(fpath, "a")
    f.write(impression + "\n")
    f.close()

'''add one visit'''
def addOneVisit():
    visits = getAllVisit()
    num = len(visits) + 1;
    fpath = os.path.join(os.path.dirname(__file__), "static", "main.txt")
    f = open(fpath, "a")
    f.write(str(num) + "\n")
    f.close()
    return str(num)

'''add one article content'''
def addArticleFile(visit, content):
    fpath = os.path.join(os.path.dirname(__file__), "static/articles", visit+".txt")
    f = open(fpath, "w")
    f.write(content)
    f.close()

'''add info'''
def addInfoFile(visit,Title,Ltitle,Sdate,Rdate):
    fpath = os.path.join(os.path.dirname(__file__), "static/info", visit+".txt")
    f = open(fpath, "w")
    f.write(Sdate + "\n" + Title + "\n" + Ltitle + "\n" + Rdate + "\n" + "0\n0")
    f.close()


'''add comment dir'''
def addCommentFile(visit):
    fpath = os.path.join(os.path.dirname(__file__), "static/comments", visit+".txt")
    f = open(fpath, "w")
    f.write("")
    f.close()


'''main page handler'''
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        num = len(getAllVisit())
        self.render("index.html",Anum=num)


'''journey handler'''
class JourneyHandler(tornado.web.RequestHandler):
    def get(self):
        visit = self.get_argument("visit", None)
        canvisit = getAllVisit()
        judge = False
        articles = getAllArticles()
        if visit in canvisit:
            next = "#"
            last = "#"
            for i in range(len(canvisit)):
                if canvisit[i] == visit:
                    break
            if (i + 1) < len(canvisit):
                next = canvisit[i+1]
            if (i - 1) >= 0:
                last = canvisit[i-1]
            judge = True
            article = getOneArticle(visit)
            comments = getAllComments(visit)
            self.render("journey.html", next=next, last=last, articles=articles, judge=judge, article=article, comments=comments, visit=visit)
        else:
            judge = False
            self.render("journey.html", judge=judge, articles=articles, visit=visit)

    def post(self):
        visit = self.get_argument("visit", None)
        Love = self.get_argument("love", None)
        Content = self.get_argument("comment", None)
        cName = self.get_secure_cookie("name")
        cPicture = self.get_secure_cookie("picture")
        if cName and cPicture:
            Name = cName
            Picture = cPicture
        else:
            Name = NAME[int(random.random()*50+1)]
            Picture = str(int(random.random()*50+1)) + ".jpg"
            self.set_secure_cookie("name", Name, expires_days=0.5)
            self.set_secure_cookie("picture", Picture)
        Class = str(int(getInfo(visit)[4])+1) + "楼"
        Date = time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time()))
        if Content:
            Content = Content.replace("\n", " ").replace(";", ",")
            comment = COMMENT(Name, Picture, Class, Date, Content)
            addOneComment(visit, comment)
            addOneCommentNum(visit)
        if Love:
            addOneLoveNum(visit)
        self.redirect("/journey?visit=" + visit)


'''wall handlers'''
class WallHandler(tornado.web.RequestHandler):
    def get(self):
        message = getAllMessage()
        impression = getAllImpression()
        self.render("wall.html", message=message, impression=impression)

    def post(self):
        Message = getAllMessage()
        Content = self.get_argument("comment", None)
        cName = self.get_secure_cookie("name")
        cPicture = self.get_secure_cookie("picture")
        if cName and cPicture:
            Name = cName
            Picture = cPicture
        else:
            Name = NAME[int(random.random()*50+1)]
            Picture = str(int(random.random()*50+1)) + ".jpg"
            self.set_secure_cookie("name", Name)
            self.set_secure_cookie("picture", Picture)
        Class = str(len(Message)+1) + "楼"
        Date = time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time()))
        if Content:
            Content = Content.replace("\n", " ").replace(";", ",")
            comment = COMMENT(Name, Picture, Class, Date, Content)
            t = Content.count("#")/2
            a = -1
            b = -1
            impression = []
            for i in range(t):
                a = Content.find("#", b+1)
                b = Content.find("#", a+1)
                if 1 < b-a < 22:
                    im = Content[a+1:b]
                    impression.append(im)
            if len(impression) > 0:
                addOneImpression(impression)
            addOneMessage(comment)
        self.redirect("/wall")

'''log in handlers'''
class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")
    def post(self):
        name = self.get_argument("name", None)
        password = self.get_argument("password", None)
        if name == "naruto" and password == "naruto":
            self.render("write.html")
        else:
            self.redirect("/login")

'''write article'''
class WriteHandler(tornado.web.RequestHandler):
    def post(self):
        title = self.get_argument("title", "None")
        ltitle = self.get_argument("ltitle", "None")
        content = self.get_argument("content", "None")
        visit = addOneVisit()
        addArticleFile(visit, content)
        Sdate = time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time()))
        Rdate = Sdate
        addInfoFile(visit, title, ltitle, Sdate, Rdate)
        addCommentFile(visit)
        self.redirect("/")


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler), (r'/journey', JourneyHandler), (r'/wall', WallHandler), (r'/login', LoginHandler), (r'/write', WriteHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True,
        cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo="
        )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
