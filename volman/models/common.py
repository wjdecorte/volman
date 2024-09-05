from datetime import datetime

from sqlalchemy import inspect

from volman.models import db
from volman.exceptions import UniqueColumnNotFoundError


class BaseColumnMixin:
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime, default=datetime.now)
    modify_date = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class TableOpsMixin:
    def as_dict(self):
        return {k: v for k, v in self.__dict__.items() if k != "_sa_instance_state"}

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def refresh(self):
        db.session.refresh(self)

    @staticmethod
    def update(updated_object):
        db.session.merge(updated_object)
        db.session.commit()

    @classmethod
    def get(cls, value):
        inspector = inspect(cls)
        keys = [col for col in inspector.columns if col.unique]
        if not keys:
            raise UniqueColumnNotFoundError(
                message=f"No unique column defined for {cls.__name__}"
            )
        return db.session.query(cls).filter(keys[0] == value).one_or_none()

    @classmethod
    def get_all(cls):
        return db.session.query(cls).all()
