import os 


basedir = os.path.abspath(os.path.dirname(__file__))

#Mac = Documents\codingtemple-july2020\week5\july2020_blog_project

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess...'