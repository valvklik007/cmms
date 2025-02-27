from app import app
from cmms import views
from flask import Blueprint


blueprint = Blueprint('index', __name__, template_folder='templates')

blueprint.add_url_rule('/', view_func=views.index, methods=['get'])
blueprint.add_url_rule('/itme/<int:id>/', view_func=views.render_item_and_update_and_delete, methods=['put', 'delete' ,'get'])
blueprint.add_url_rule('/itme/<int:id>/notepad/', view_func=views.notepad, methods=['post' ,'get'])
blueprint.add_url_rule('/itme/<int:id>/manual/', view_func=views.manual_book, methods=['post' ,'get', 'delete'])
blueprint.add_url_rule('/itme/add/', view_func=views.add_item, methods=['post', 'get'])
blueprint.add_url_rule('/add_option/<data>/', view_func=views.add_delete_option, methods=['get', 'post'])
blueprint.add_url_rule('/maintenance/<int:id>/', view_func=views.maintenance, methods=['get', 'post'])