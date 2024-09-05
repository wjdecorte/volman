
from sqlalchemy.orm import relationship

from volman.models import db
from volman.models.common import BaseColumnMixin, TableOpsMixin


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


class Volunteer(TableOpsMixin, BaseColumnMixin):
    __tablename__ = "volunteer"

    first_name = db.Column(db.db.String(100))
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


class Contact(TableOpsMixin, BaseColumnMixin):
    __tablename__ = "contact"

    volunteer_id = db.Column(db.Integer, db.ForeignKey("volunteer.id"))


class Team(TableOpsMixin, BaseColumnMixin):
    __tablename__ = "team"

    team_name = db.Column(db.String(500))


class Skill(TableOpsMixin, BaseColumnMixin):
    __tablename__ = "skill"

    skill_name = db.Column(db.String(500))
