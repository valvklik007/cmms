from flask import request, render_template, url_for, session
import datetime, time

from mypy.nodes import set_flags
from sqlalchemy.dialects.postgresql import psycopg_async
from sqlalchemy.inspection import inspect

from app import db, turbo
import inspect

from cmms import models



def request_db(data):
    for m in inspect.getmembers(models):
        if data.lower() == m[0].lower():
            return getattr(models, m[0])


class BaseRepository:
    def __init__(self, model):
        self._db = db.session
        self._model = model

    def add(self, **kwargs):
        item = self._model(**kwargs)
        self._db.add(item)
        self._db.commit()

        return item

    def delete(self, id_item):
        item = self._model.query.filter_by(id = id_item).first()
        if item:
            self._db.delete(item)
            self._db.commit()
            return True

    def get_all(self):
        return self._db.query(self._model).all()

    def get_filter(self, **kwargs):
        return self._db.query(self._model).filter_by(**kwargs).all()

    def property_parent(self, name):
        relationship = getattr(self._model, name)
        # Имя родителя
        parent_table_name = relationship.property.mapper.class_.__table__.name
        return parent_table_name



class ManufacturerItme(BaseRepository):
    def __init__(self):
        super().__init__(models.ManufacturerItme)

    def add_parent(self, name, fk):
        self.add(name=name, fk_ModelItme=fk)


class ModelItme(BaseRepository):
    def __init__(self):
        super().__init__(models.ModelItme)


class StatusItme(BaseRepository):
    def __init__(self):
        super().__init__(models.StatusItme)


class ConditionItme(BaseRepository):
    def __init__(self):
        super().__init__(models.ConditionItme)


class TypeEquipment(BaseRepository):
    def __init__(self):
        super().__init__(models.TypeEquipment)


class PlaceOperation(BaseRepository):
    def __init__(self):
        super().__init__(models.PlaceOperation)


name_table ={
    'manufactureritme' : ManufacturerItme(),
    'modelitme' : ModelItme(),
    'statusitme' : StatusItme(),
    'conditionitme': ConditionItme(),
    'typeequipment' : TypeEquipment(),
    'placeoperation' : PlaceOperation(),
}


"""Главная страница"""
def index():
    return render_template('/cmms/index.html')


def add_and_delete_item(req):
    pass

def add_item():
    if request.method == 'GET':
        tem_context =  dict(
            manufactureritme = ManufacturerItme().get_all(),
            modelitme = ModelItme().get_all(),
            statusitme = StatusItme().get_all(),
            conditionitme= ConditionItme().get_all(),
            typeequipment = TypeEquipment().get_all(),
            placeoperation = PlaceOperation().get_all(),
            data_time = datetime.datetime.now().strftime("%Y-%m-%d"),
        )
        return render_template('/cmms/item.html', **tem_context)
    if request.method == 'POST':
        # manufactureritme
        pass


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


def push_update(template, **kwargs):
    turbo.push(
        turbo.update(
            render_template(
                template,
                **kwargs),
            target=kwargs['target'],),
    )

def push_append(template, **kwargs):
    turbo.push(
        turbo.append(
            render_template(
                template,
                **kwargs),
            target=kwargs['target'],),
    )

def add_delete_option(data):
    parent_records = None
    if request.method == "POST":
        if request.form['action'] == 'add':
            if 'modelitme' in data:
                name_table[data].add(name = request.form['option'], fk_ModelItme = request.form['parent'])
            else:
                name_table[data].add(name = request.form['option'])

            data_dict = dict(
                option_values= name_table[data].get_filter(name = request.form['option']),
                target=data,
            )

            if turbo.can_stream():
                push_append(template='/cmms/include/add_option_value.html', **data_dict),
                return []

        elif request.form['action'] == 'delete':
            for m in request.form.getlist('allocated_name'):
                name_table[data].delete(m)

    if request.values.get('id') is not None:
        if 'modelitme' in data:
            option_values = name_table[data].get_filter(fk_ModelItme = request.values.get('id'))
            parent_records = name_table[name_table[data].property_parent('parent')].get_all()
    else:
        option_values = name_table[data].get_all()

    data_dict = dict(
        option_values=option_values,
        parent_records=parent_records,
        id_parent = request.values.get('id'),
        target=data,
    )

    if turbo.can_stream():
        push_update(template='/cmms/include/add_option_value.html', **data_dict),
        return []
    else:
        return render_template('/cmms/add_option.html', **data_dict)

