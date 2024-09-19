from datetime import date, datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase

from sqlalchemy import inspect

from volman.exceptions import UniqueColumnNotFoundError


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


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


volunteer_to_team_bridge = db.Table(
    "volunteer_to_team_bridge",
    db.metadata,
    db.Column("volunteer_id", db.Integer, db.ForeignKey("volunteer.id")),
    db.Column("team_id", db.Integer, db.ForeignKey("team.id")),
)

volunteer_to_skill_bridge = db.Table(
    "volunteer_to_skill_bridge",
    db.metadata,
    db.Column("volunteer_id", db.Integer, db.ForeignKey("volunteer.id")),
    db.Column("skill_id", db.Integer, db.ForeignKey("team.id")),
)


class Volunteer(BaseColumnMixin, TableOpsMixin, db.Model):
    first_name = db.Column(db.String(100))
    middle_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    full_name = db.Column(db.String(300))
    cell_phone = db.Column(db.String(10))
    email = db.Column(db.String(500))
    address_line_1 = db.Column(db.String(100))
    address_line_2 = db.Column(db.String(100))
    city = db.Column(db.String(100))
    county = db.Column(db.String(50))
    state = db.Column(db.String(2))
    zipcode = db.Column(db.String(10))
    home_phone = db.Column(db.String(12))
    work_phone = db.Column(db.String(12))
    cell_phone = db.Column(db.String(12))
    ishelters_id = db.Column(db.Integer)
    ishelters_created_by_id = db.Column(db.Integer)
    ishelters_created_dt = db.Column(db.DateTime)
    ishelters_category_type = db.Column(db.String(100))
    application_received_date = db.Column(db.Date)

    contact_entries = relationship(
        "Contact",
        backref="volunteer",
        lazy=True,
        cascade="all, delete-orphan",
    )


class Contact(BaseColumnMixin, TableOpsMixin, db.Model):
    # volunteer_id = db.Column(db.Integer, db.ForeignKey("volunteer.id"))
    contact_date: Mapped[date]
    contact_notes: Mapped[str]


class Team(BaseColumnMixin, TableOpsMixin, db.Model):
    __tablename__ = "team"

    team_name = db.Column(db.String(500))


class Skill(BaseColumnMixin, TableOpsMixin, db.Model):
    __tablename__ = "skill"

    skill_name = db.Column(db.String(500))
