from app import app
from cmms.url import blueprint as cmss


app.register_blueprint(cmss, url_prefix="/")


