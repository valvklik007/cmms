import re, os
import string
from fileinput import filename
from idlelib.rpc import request_queue
import random
from re import template

from flask import request, render_template, url_for, session, redirect
import datetime, time

from mypy.nodes import set_flags
from sqlalchemy.dialects.postgresql import psycopg_async
from sqlalchemy.inspection import inspect
from sqlalchemy import ForeignKey
from sqlalchemy.orm import joinedload

from werkzeug.utils import secure_filename

from app import db, turbo, app
import inspect

from cmms import models



def request_db(data):
    for m in inspect.getmembers(models):
        if data.lower() == m[0].lower():
            return getattr(models, m[0])


def req_litter(req):
    request_key = {}
    for key, value in req.form.items():
        request_key.update({key: value})
    return request_key

# def is_foreign_key(column):
#     # Проверяем, является ли тип столбца ForeignKey
#     return any(isinstance(constraint, ForeignKey) for constraint in column.foreign_keys)


class BaseRepository:
    def __init__(self, model):
        self._db = db.session
        self._model = model

    def add(self, **kwargs):
        item = self._model(**kwargs)
        try:
            self._db.add(item)
            self._db.commit()
        except Exception as e:
            self._db.rollback()
        return item

    def update(self, item, **kwargs):
        # item = self._model.query.filter_by(id=id_i)
        try:
            item.update({**kwargs})
            self._db.commit()
        except:
            self._db.rollback()

    def delete(self, id_item):
        item = self._model.query.filter_by(id = id_item).first()
        if item:
            try:
                self._db.delete(item)
                self._db.commit()
                return True
            except Exception as e:
                self._db.rollback()
                return False

    def que(self):
        #запрос
        return self._db.query(self._model)

    def get_all(self):
        # Выбора всей таблицы
        return self._db.query(self._model).all()

    def get_filter(self, **kwargs):
        #Сформулировать запрос и вывести
        return self._db.query(self._model).filter_by(**kwargs)

    def property_parent(self, name):
        relationship = getattr(self._model, name)
        # Имя родителя
        parent_table_name = relationship.property.mapper.class_.__table__.name
        return parent_table_name

    # def get_attributes(self):
    #     attributes = []
    #     for column in self._model.__table__.columns:
    #         attr_info = {
    #             "name": column.name,
    #             "type": str(column.type),
    #             "is_foreign_key": is_foreign_key(column),  # Проверяем, является ли внешним ключом
    #         }
    #         attributes.append(attr_info)
    #     return attributes


class ManufacturerItme(BaseRepository):
    def __init__(self):
        super().__init__(models.ManufacturerItme)

    # def add_parent(self, name, fk):
    #     self.add(name=name, fk_ModelItme=fk)



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

class Item(BaseRepository):
    def __init__(self):
        super().__init__(models.Item)


class Notepad(BaseRepository):
    def __init__(self):
        super().__init__(models.Notepad)

class ManualBook(BaseRepository):
    def __init__(self):
        super().__init__(models.ManualBook)


name_table ={
    'manufactureritme' : ManufacturerItme(),
    'modelitme' : ModelItme(),
    'statusitme' : StatusItme(),
    'conditionitme': ConditionItme(),
    'typeequipment' : TypeEquipment(),
    'placeoperation' : PlaceOperation(),
}


"""Контекст для карточки товара"""
def context_template_item():
    # Получаем контекст
    tem_context = dict(
        manufactureritme=ManufacturerItme().get_all(),
        modelitme=ModelItme().get_all(),
        statusitme=StatusItme().get_all(),
        conditionitme=ConditionItme().get_all(),
        typeequipment=TypeEquipment().get_all(),
        placeoperation=PlaceOperation().get_all(),
        data_time=datetime.datetime.now().strftime("%Y-%m-%d"),
    )
    return tem_context


"""Главная страница"""
def index():
    return render_template('/cmms/index.html')


"Добавления карточки оборудования"
def add_item():
    if request.method == 'GET':
        tem_context = context_template_item()
        return render_template('/cmms/item.html', **tem_context)
    if request.method == 'POST':
        rq = req_litter(request)
        exploitation_date = datetime.datetime.strptime(rq['exploitation'], '%Y-%m-%d').date()
        rq['exploitation'] = exploitation_date
        id_add = Item().add(**rq)
        return redirect(url_for('index.render_item_and_update_and_delete', id=id_add.id), 303)


"Редактирования и удаления карточки оборудования"
def render_item_and_update_and_delete(id):
    item = Item().que().get(id)
    if item is not None:
        if request.method == 'GET':
            tem_context = context_template_item()
            item = Item().get_filter(id=id).first()
            tem_context.update(item = item)
            return render_template('/cmms/item.html', **tem_context)
        if request.method == 'PUT':
            rq = req_litter(request)
            exploitation_date = datetime.datetime.strptime(rq['exploitation'], '%Y-%m-%d').date()
            rq['exploitation'] = exploitation_date
            item = Item().get_filter(id=id)
            Item().update(item, **rq)
            return []
        if request.method == 'DELETE':
            Item().delete(id)
            return redirect(url_for('index.add_item'), 303)
    else:
        return redirect(url_for('index.add_item'))


"""Блокнот карточки"""
def notepad(id):
    item = Item().que().get(id)
    if item is not None:
        if request.method == 'POST':
            rq = req_litter(request)
            q = Notepad().get_filter(fk_item=id)
            if q.first() is not None:
                q = Notepad().get_filter(fk_item=id)
                Notepad().update(q, **rq)
            else:
                Notepad().add(**rq)
        return render_template('/cmms/notepad.html', item=item)
    else:
        return redirect(url_for('index.add_item'))


"""Обслуживание"""
def maintenance(id):

    return render_template('cmms/to_add_edit.html')


"""Рандом"""
def ran(i):
    a = string.ascii_lowercase
    c = string.digits
    n = ""
    for sim_1 in range(i):
        n = n + random.choice(a + c)
    return n


"""Документация"""
def manual_book(id):
    item = Item().que().get(id)
    if item is not None:
        if request.method == 'DELETE':
            print(request.form['delete'])
            ManualBook().delete(request.form['delete'])
            return redirect(url_for('index.manual_book', id=item.id), 201)
        elif request.method == 'POST':
            file = request.files.getlist('files')
            for m in file:
                re_f = re.sub(r'[\]\[\/\\;,><&*:%=+@!#{}^()|?^ ]', '-', m.filename)
                file = f"{item.name}-{ran(10)}-{re_f}"
                m.save(os.path.join(app.config['UPLOAD_FOLDER'], file))
                ManualBook().add(**dict(slug = file, fk_item = id,))

            return redirect(url_for('index.manual_book', id=item.id))

        return render_template('/cmms/manual.html', item=item)
    return redirect(url_for('index.add_item'))


"Стримы turbo flask"
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


"Общая модификация параметров. Добавления, удаления, однотипных таблиц"
def add_delete_option(data):
    parent_records = None
    data_dict = dict(
        target=data,
    )
    if request.method == "POST":
        if request.form['action'] == 'add':
            request_key = {}
            for key, value in request.form.items():
                if 'action' not in key:
                    request_key.update({key: value})
            it = name_table[data].add(**request_key)
            data_dict.update(option_values = name_table[data].get_filter(**request_key).all(),)

            if turbo.can_stream():
                push_append(template='/cmms/include/add_option_value.html', **data_dict),
                return []

        elif request.form['action'] == 'delete':
            for m in request.form.getlist('allocated_name'):
                name_table[data].delete(m)

    if request.values.get('id') is not None:
        if 'modelitme' in data:
            option_values = name_table[data].get_filter(fk_ModelItme = request.values.get('id')).all()
            parent_records = name_table[name_table[data].property_parent('parent')].get_all()
    else:
       option_values = name_table[data].get_all()

    data_dict.update(
        option_values=option_values,
        parent_records=parent_records,
        id_parent = request.values.get('id'),
    )

    if turbo.can_stream():
        push_update(template='/cmms/include/add_option_value.html', **data_dict),
        return []
    else:
        return render_template('/cmms/add_option.html', **data_dict)

