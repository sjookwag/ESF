import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  SECRET_KEY = os.urandom(32) #os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'site.db')  #os.environ.get('DATABASE_URL')
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = 'sjoo.kwag@gmail.com' #os.environ.get('EMAIL_USER')
  MAIL_PASSWORD = 'jimsjoo78445' #os.environ.get('EMAIL_PASS')
  MEDIA = os.path.join(basedir, '/media')
  