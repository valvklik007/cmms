from app import db
from datetime import datetime
import re
from sqlalchemy import Table, Column, Integer, String, DateTime


# def slugify(s):
#     pattern = r'[^\w+]'
#     return re.sub(pattern, '-', s)


"""Производитель"""
class ManufacturerItme(db.Model):
    __tablename__ = 'manufactureritme'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    modelitme_relationship = db.relationship('ModelItme', backref='parent', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Name:{self.name}>'


"""Модель"""
class ModelItme(db.Model):
    __tablename__ = 'modelitme'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    fk_ModelItme = db.Column(db.Integer, db.ForeignKey('manufactureritme.id'), nullable=False)



    def __repr__(self):
        return f'<Name:{self.name}>'

"""Статус"""
class StatusItme(db.Model):
    __tablename__ = 'statusitme'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return f'<Name:{self.name}>'


"""Тип оборудования"""
class TypeEquipment(db.Model):
    __tablename__ = 'typeequipment'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return f'<Name:{self.name}>'


"""Место"""
class PlaceOperation(db.Model):
    __tablename__ = 'placeoperation'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return f'<Name:{self.name}>'


"""Состояние"""
class ConditionItme(db.Model):
    __tablename__ = 'conditionitme'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return f'<Name:{self.name}>'


"""Блокнот"""
class Notepad(db.Model):
    __tablename__ = 'notepad'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, default=None)
    fk_item = db.Column(db.Integer, db.ForeignKey('item.id', ondelete='CASCADE'), nullable=False, unique=True)

    item = db.relationship('Item', back_populates='notepad')

    def __repr__(self):
        return f'<text:{self.text}>'


"""Мануалы"""
class ManualBook(db.Model):
    __tablename__ = 'manualbook'
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(30), unique=True)
    fk_item = db.Column(db.Integer, db.ForeignKey('item.id', ondelete='CASCADE'), nullable=False)

    item = db.relationship('Item', back_populates='manualbook')

    def __repr__(self):
        return f'<slug:{self.slug}>'


"""Регламент работ"""
class RegulatoryWork(db.Model):
    __tablename__ = 'regulatorywork'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    maintenance = db.relationship('Maintenance', back_populates='regulatory_work')

    def __repr__(self):
        return f'<Name:{self.name}>'


"""Расписания"""
class Schedules(db.Model):
    __tablename__ = 'schedules'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    period = db.Column(db.String(7))
    date_time = db.Column(db.SmallInteger)

    maintenance = db.relationship('Maintenance', back_populates='schedules')

    def __repr__(self):
        return f'<Name:{self.name}>'


"""Обслуживание"""
class Maintenance(db.Model):
    __tablename__ = 'maintenance'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    data_time = db.Column(db.Date, default=datetime.today)
    data_time_old = db.Column(db.Date, default=datetime.today)
    check_work = db.Column(db.Boolean, default=False)
    fk_schedule = db.Column(db.Integer, db.ForeignKey('schedules.id', ondelete='SET NULL'), nullable=False)
    fk_regulatory_work = db.Column(db.Integer, db.ForeignKey('regulatorywork.id', ondelete='SET NULL'), nullable=False)
    fk_item = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)

    schedules = db.relationship("Schedules", back_populates='maintenance')
    regulatory_work = db.relationship("RegulatoryWork", back_populates='maintenance')
    item = db.relationship("Item", back_populates='maintenance')

    def __repr__(self):
        return f'<Name:{self.name}>'



"""Карточка оборудования"""
class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, default=None)
    weight = db.Column(db.Float, default=None)
    price = db.Column(db.Float, default=None)
    exploitation = db.Column(db.Date, default=datetime.today)
    serial_num = db.Column(db.String(150), default=None)
    warranty = db.Column(db.Date, default=datetime.today)
    date_product = db.Column(db.Date, default=datetime.today)

    fk_ModelItme = db.Column(db.Integer, db.ForeignKey('modelitme.id', ondelete='SET NULL'), nullable=True)
    fk_StatusItme = db.Column(db.Integer, db.ForeignKey('statusitme.id', ondelete='SET NULL'), nullable=True)
    fk_ConditionItme = db.Column(db.Integer, db.ForeignKey('conditionitme.id', ondelete='SET NULL'), nullable=True)
    fk_TypeEquipment = db.Column(db.Integer, db.ForeignKey('typeequipment.id', ondelete='SET NULL'), nullable=True)
    fk_PlaceOperation = db.Column(db.Integer, db.ForeignKey('placeoperation.id', ondelete='SET NULL'), nullable=True)

    model_item = db.relationship("ModelItme", backref="items")
    model_StatusItme = db.relationship("StatusItme", backref="items")
    model_ConditionItme = db.relationship("ConditionItme", backref="items")
    model_TypeEquipment = db.relationship("TypeEquipment", backref="items")
    model_PlaceOperation = db.relationship("PlaceOperation", backref="items")
    notepad = db.relationship('Notepad', back_populates='item', uselist=False, cascade='all, delete-orphan')
    manualbook = db.relationship('ManualBook', back_populates='item', uselist=True, cascade='all, delete-orphan')
    maintenance = db.relationship('Maintenance', back_populates='item', cascade='all, delete-orphan')


    def __repr__(self):
        return f'<Name:{self.name}>'



