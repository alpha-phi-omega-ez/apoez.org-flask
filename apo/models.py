from flask_login import UserMixin

from apo import db


class User(db.Model, UserMixin):
    id = db.Column(db.String(50), primary_key=True, unique=True)
    name = db.Column(db.String(50), nullable=False, unique=False)
    email = db.Column(db.String(50), nullable=False, unique=True)


# Backtest Classes Table
class BacktestClasses(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    subject_code = db.Column(db.String(4), nullable=False, unique=False)
    course_number = db.Column(db.Integer, nullable=False, unique=False)
    name_of_class = db.Column(db.String(150), nullable=False, unique=False)
    is_alias = db.Column(db.Boolean, nullable=False, unique=False)
    alias_subject_code = db.Column(db.String(4), nullable=True, unique=False)
    alias_course_number = db.Column(db.Integer, nullable=True, unique=False)


# Backtest Table
# Spring semester denoted a for proper sorting
class Backtest(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    added = db.Column(db.Date, nullable=False, unique=False)
    subject_code = db.Column(db.String(4), nullable=False, unique=False)
    course_number = db.Column(db.Integer, nullable=False, unique=False)
    name_of_class = db.Column(db.String(150), nullable=False, unique=False)
    exam = db.Column(db.Boolean, unique=False, default=False)
    quiz = db.Column(db.Boolean, unique=False, default=False)
    midterm = db.Column(db.Boolean, unique=False, default=False)
    year = db.Column(db.Integer, nullable=False, unique=False)
    semester = db.Column(db.Integer, nullable=False, unique=False) # 1 = Spring, 2 = Summer, 3 = Fall
    backtest_number = db.Column(db.Integer, nullable=False, unique=False) # E1 E2 Q1 etc
    backtest_count = db.Column(db.Integer, nullable=False, unique=False) # quantitiy


# Backtest Table
# Spring semester denoted a for proper sorting
class Chargers(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    in_office = db.Column(db.Boolean, nullable=False, unique=False)
    checked_out = db.Column(db.DateTime, nullable=False, unique=False)
    description = db.Column(db.Text, nullable=False, unique=False)
    phone_area_code = db.Column(db.Integer, nullable=True, unique=False)
    phone_middle = db.Column(db.Integer, nullable=True, unique=False)
    phone_end = db.Column(db.Integer, nullable=True, unique=False)


# Lost Reports Table
# class LostReport(db.Model):
#     id = db.Column(db.Integer, primary_key=True, unique=True)
#     first_name = db.Column(db.String(40), nullable=False, unique=False)
#     last_name = db.Column(db.String(50), nullable=False, unique=False)
#     email = db.Column(db.String(100), nullable=False, unique=False)
#     phone_area_code = db.Column(db.Integer, nullable=False, unique=False)
#     phone_middle = db.Column(db.Integer, nullable=False, unique=False)
#     phone_end = db.Column(db.Integer, nullable=False, unique=False)
#     description = db.Column(db.Text, nullable=False, unique=False)
#     item_type = db.Column(db.String(15), nullable=False, unique=False)
#     locations = db.Column(db.Text, nullable=False, unique=False)
#     date_lost = db.Column(db.Date, nullable=False, unique=False)
#     date_added = db.Column(db.Date, nullable=False, unique=False)


# class LostItem(db.Model):
#     id = db.Column(db.Integer, primary_key=True, unique=True)
#     description = db.Column(db.Text, nullable=False, unique=False)
#     lost_report_match = db.Column(db.Integer, db.ForeignKey('lostreport.id'), unique=False, nullable=True)
#     item_type = db.Column(db.String(15), nullable=False, unique=False)
#     locations = db.Column(db.Text, nullable=False, unique=False)
#     date_lost = db.Column(db.Date, nullable=False, unique=False)
