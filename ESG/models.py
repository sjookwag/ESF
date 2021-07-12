from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from ESG import db, login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model, UserMixin):
  __tablename__ = 'user'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
  password = db.Column(db.String(60), nullable=False)
  posts = db.relationship('Post', backref='author', lazy=True)
  models = db.relationship('Model', backref='author', lazy=True)
  
  def get_reset_token(self, expires_sec=1800):
    s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
    return s.dumps({'user_id': self.id}).decode('utf-8')

  @staticmethod
  def verify_reset_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
      user_id = s.loads(token)['user_id']
    except:
      return None
    return User.query.get(user_id)

  def __repr__(self):
    return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Model(db.Model):
  __tablename__ = 'model'
  id       = db.Column(db.Integer, primary_key=True)
  modelname= db.Column(db.String(100))  
  category = db.Column(db.Integer)
  fdist    = db.Column(db.String(3))
  param10  = db.Column(db.Float)
  param20  = db.Column(db.Float)
  sdist    = db.Column(db.String(3))
  param11  = db.Column(db.Float)
  param21  = db.Column(db.Float)
  param31  = db.Column(db.Float)
  user_id  = db.Column(db.Integer, db.ForeignKey('user.id'))
  cates = db.relationship('Category')
  dists = db.relationship('Distribution')
  
  def __repr__(self):
    return f"Model('{self.modelname}', '{self.category}')"

class Category(db.Model):
  __tablename__ = 'category'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)  
  description = db.Column(db.String(100), nullable=True)
  abbr = db.Column(db.String(3), db.ForeignKey('model.category'), nullable=False)    
  # models = db.relationship('Model', backref='category', lazy=True)

  def __repr__(self):
    return f"Category('{self.name}', '{self.description}')"

class Distribution(db.Model):
  __tablename__ = 'distribution'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)  
  type = db.Column(db.String(10), nullable=True)
  params = db.Column(db.Integer, nullable=False)
  abbr = db.Column(db.String(3), db.ForeignKey('model.fdist'), nullable=False)
  # models = db.relationship('Model', backref='distribution', lazy=True)

  def __repr__(self):
    return f"Distribution('{self.name}', '{self.type}')"
    
class Post(db.Model):
  __tablename__ = 'post'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  content = db.Column(db.Text, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  def __repr__(self):
    return f"Post('{self.title}', '{self.date_posted}')"