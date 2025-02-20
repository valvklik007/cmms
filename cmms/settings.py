from datetime import timedelta

class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///cmms.bd'
    SECRET_KEY = '$d9wr)1=7l11*_!gn*%mkok8nx*ci%fqm3(hh*i__(x9&u%do#'
    # REMEMBER_COOKIE_SECURE = False
    # PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)