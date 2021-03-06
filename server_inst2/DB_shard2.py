from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


DATABASE = 'Expense_shard2'
PASSWORD = 'admin'
USER = 'root'
HOSTNAME = 'localhost'



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s'%(USER, PASSWORD, HOSTNAME, DATABASE)
db = SQLAlchemy(app)


class CreateDB():
	def __init__(self):
		import sqlalchemy
		engine = sqlalchemy.create_engine('mysql://%s:%s@%s'%(USER, PASSWORD, HOSTNAME)) # connect to server
		engine.execute("CREATE DATABASE IF NOT EXISTS %s "%(DATABASE)) #create db


class ExpenseSchema(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	email = db.Column(db.String(80))
	category = db.Column(db.String(80))
	description = db.Column(db.String(80))
	link = db.Column(db.String(80))
	estimated_costs= db.Column(db.String(80))
	submit_date=db.Column(db.String(80))
	status= db.Column(db.String(80))
	decision_date=db.Column(db.String(80))


	def __init__(self,id,name,email,category,description,link,estimated_costs,submit_date,status,decision_date):
		self.id = id
		self.name = name
		self.email = email
		self.category = category
		self.description = description
		self.link = link
		self.estimated_costs = estimated_costs
		self.submit_date = submit_date
		self.status = status
		self.decision_date = decision_date

