import cgi
import datetime
import urllib
import wsgiref.handlers
import web
import time
from google.appengine.ext import db
from datetime import date
from datetime import timedelta
from google.appengine.api import mail

urls = (
	'/', 'index',
	'/note', 'note',
	'/source', 'source',
	'/task','task',
	'/crash', 'crash'
)

render = web.template.render('templates/')
class Note(db.Model):
	actualDate = db.DateProperty()
	expectedDate=db.DateProperty()
notes = db.GqlQuery("SELECT * FROM Note ORDER BY actualDate DESC LIMIT 10")

class task:
	def GET(self):
		today=date.today()
		if(notes.count()>0):
			nextday=notes[0].expectedDate
			t=nextday-today
			if(t.days==4):
				mail.send_mail(sender="kamelzcs@gmail.com",
								to="chensi910@gmail.com",
								subject="Probability I will come in four days",
								body="""
				Dear Si:

				Wish you all the best.
                http://pynotes123.appspot.com
				Yours,Shuai
				""")
		return web.seeother('/')

class task2:
	def GET(self):
				mail.send_mail(sender="kamelzcs@gmail.com",
								to="chensi910@gmail.com",
								subject="Probability I will come in four days",
								body="""
				Dear Si:

				Wish you all the best.

				Yours,Shuai
				""")
				return web.seeother('/')

class index:
	def GET(self):
		return render.index(notes)

class note:
    def POST(self):
		content = web.input()
		note = Note()
		note.actualDate =date(int(content.year),int(content.month),int(content.day))
		computes=[0.2,0.1,0.1]
		expectedSum=0
		tp=notes.count()
		if notes.count() >=4:
				tp=4
				for i in range(3):
					d=notes[i].actualDate-notes[i+1].actualDate
					expectedSum=expectedSum+computes[i]*int(d.days)
				d=note.actualDate-notes[0].actualDate
				expectedSum=expectedSum+0.6*(d.days)

		elif notes.count()>=1:
				for i in range(notes.count()-1):
					d=notes[i].actualDate-notes[i+1].actualDate
					expectedSum=expectedSum+int(d.days)
				d=note.actualDate-notes[0].actualDate
				expectedSum=expectedSum+int(d.days)
				expectedSum=expectedSum*1.0/(notes.count())

		else:
			expectedSum=30


		expectedSum=min(expectedSum,40)
		temp=timedelta(days=expectedSum)
		note.expectedDate=note.actualDate+temp
		note.put()
		return web.seeother('/')

class source:
    def GET(self):
        web.header('Content-Type', 'text/plain')
        return (
          '## index.py\n\n' +
          file('index.py').read() +
          '\n\n## templates/index.html\n\n' +
		  file('templates/index.html').read()+
		  '\n\n## app.yaml\n\n' +
          file('app.yaml').read()+
		  '\n\n## cron.yaml\n\n' +
          file('cron.yaml').read()
        )

class crash:
    def GET(self):
        import logging
        logging.error('test')
        crash

app = web.application(urls, globals())
main = app.cgirun()
