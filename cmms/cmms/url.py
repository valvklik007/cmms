from app import app
from cmms import views
from flask import Blueprint


blueprint = Blueprint('index', __name__, template_folder='templates')

blueprint.add_url_rule('/', view_func=views.index, methods=['get'])
blueprint.add_url_rule('/itme/<int:id>/', view_func=views.render_and_update_item, methods=['put', 'delete' ,'get'])
blueprint.add_url_rule('/itme/<int:id>/notepad/', view_func=views.notepad, methods=['post' ,'get'])
blueprint.add_url_rule('/itme/add/', view_func=views.add_item, methods=['post', 'get'])
blueprint.add_url_rule('/add_option/<data>/', view_func=views.add_delete_option, methods=['get', 'post'])
blueprint.add_url_rule('update_models/<int:id>/', view_func=views.update_model_item, methods=['get'])


# blueprint.add_url_rule('/dig_sum_item', view_func=views.dig_sum_item, methods=['get'])
# blueprint.add_url_rule('/dig_sum_item_agent', view_func=views.dig_sum_item_agent, methods=['get'])
# blueprint.add_url_rule('/sum_dig', view_func=views.dig, methods=['get'])