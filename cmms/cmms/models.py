from app import db
from datetime import datetime
import re
from sqlalchemy import Table, Column, Integer, String, DateTime


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)

# Таблицы для item
class ManufacturerItme(db.Model):
    __tablename__ = 'manufactureritme'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    modelitme_relationship = db.relationship('ModelItme', backref='parent', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Name:{self.name}>'


class ModelItme(db.Model):
    __tablename__ = 'modelitme'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    fk_ModelItme = db.Column(db.Integer, db.ForeignKey('manufactureritme.id'), nullable=False)



    def __repr__(self):
        return f'<Name:{self.name}>'


class StatusItme(db.Model):
    __tablename__ = 'statusitme'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return f'<Name:{self.name}>'


class TypeEquipment(db.Model):
    __tablename__ = 'typeequipment'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return f'<Name:{self.name}>'


class PlaceOperation(db.Model):
    __tablename__ = 'placeoperation'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return f'<Name:{self.name}>'


class ConditionItme(db.Model):
    __tablename__ = 'conditionitme'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return f'<Name:{self.name}>'


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, default=None)
    weight = db.Column(db.Float, default=None)
    price = db.Column(db.Float, default=None)
    exploitation = db.Column(db.Date, default=datetime.today)
    fk_ManufacturerItme = db.Column(db.Integer, db.ForeignKey('manufactureritme.id'), nullable=False)
    fk_StatusItme = db.Column(db.Integer, db.ForeignKey('statusitme.id'), nullable=False)
    fk_ConditionItme = db.Column(db.Integer, db.ForeignKey('conditionitme.id'), nullable=False)
    fk_TypeEquipment = db.Column(db.Integer, db.ForeignKey('typeequipment.id'), nullable=False)
    fk_PlaceOperation = db.Column(db.Integer, db.ForeignKey('placeoperation.id'), nullable=False)

    def __repr__(self):
        return f'<Name:{self.name}>'



