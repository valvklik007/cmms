from flask import request, render_template, url_for, session
import datetime, time

from sqlalchemy.inspection import inspect

from app import db, turbo
import inspect

from cmms import models



def request_db(data):
    for m in inspect.getmembers(models):
        if data.lower() == m[0].lower():
            return getattr(models, m[0])

"""Главная страница"""
def index():
    return render_template('/cmms/index.html')


def add_item():
    tem_context =  dict(
        name_table ={
            'ManufacturerItme' : 'manufactureritme',
            'ModelItme' : 'modelitme',
            'StatusItme' : 'statusitme',
            'ConditionItme': 'conditionitme',
            'TypeEquipment' : 'typeequipment',
            'PlaceOperation' : 'placeoperation',
         },
        manufactureritme = models.ManufacturerItme.query.all(),
        modelitme = models.ModelItme.query.all(),
        statusitme = models.StatusItme.query.all(),
        conditionitme=models.ConditionItme.query.all(),
        typeequipment = models.TypeEquipment.query.all(),
        placeoperation = models.PlaceOperation.query.all(),
        data_time = datetime.datetime.now().strftime("%Y-%m-%d"),
    )

    return render_template('/cmms/item.html', **tem_context)

def item(id):

    return render_template('/cmms/item.html')


def update_model_item(id):
    model = models.ModelItme.query.filter_by(fk_ModelItme = id).all()

    # model = models.ManufacturerItme.query.filter(ModelItme.id == id).all()
    print(model)
    if model is None:
        return ''
    else:
        return f"<p>{model}</p>"


def get_parent_table(model):
    """Определяет родительскую таблицу по ForeignKey"""
    mapper = db.inspect(model)  # Получаем маппер SQLAlchemy
    for rel in mapper.columns.values():
        if rel.foreign_keys:  # Проверяем, если есть внешний ключ
            # print(rel.name)
            return request_db(next(iter(rel.foreign_keys)).column.table.name), rel.name
    return None, None


def push_update(template, **data_dict):
    turbo.push(
        turbo.update(
            render_template(
                template,
                **data_dict),
            target=data_dict['target'],),
    )

def add_delete_option(data):
    # try:
    data_models = request_db(data)
    parent_model, name_fk = get_parent_table(data_models)
    parent_records = parent_model.query.all() if parent_model else None

    if request.method == "POST":
        data_models_action = data_models()
        if request.form['action'] == 'add':
            if parent_records:
                setattr(data_models_action, name_fk, request.form['parent'])

            data_models_action.name = request.form['option']
            db.session.add(data_models_action)
            db.session.flush()
            db.session.commit()
        elif request.form['action'] == 'delete':
            for m in request.form.getlist('allocated_name'):
                db.session.delete(data_models_action.query.filter_by(id = m).one())
                db.session.commit()
    id_parent =  request.values.get('id')
    if parent_records:
        if id_parent is not None:
            option_values = data_models.query.filter(getattr(data_models, name_fk) == id_parent).all()
        else:
            try:
                option_values = data_models.query.filter(getattr(data_models, name_fk) == request.form['parent']).all()
            except:
                option_values = data_models.query.all()
    else:
        option_values = data_models.query.all()

    data_dict = dict(
        # option_values=data_models.query.all(),
        option_values=option_values,
        parent_records=parent_records,
        id_parent = id_parent,
        target=data,
    )

    if turbo.can_stream():
        push_update(template='/cmms/include/add_option_value.html', **data_dict),
        return []
    else:
        return render_template('/cmms/add_option.html', **data_dict)


    # except Exception as err:
    #     print(err)
    #     return "404", 400

