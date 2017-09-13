"""defines the models for the public pages
"""
from datetime import date
from flaskserver.extensions import db

class BetaSignUps(db.Model):
    """stores the emails for users who sign up for the closed beta
    """
    __tablename__ = "beta_sign_ups"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    signup_date = db.Column(db.Date, default=date.today())

class ContactUsMessages(db.Model):
    """stores the messages that the users have sent on the Contact_Us page
    """
    __tablename__ = "contact_us_messages"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.String(255))
    phone = db.Column(db.Integer)
    subject = db.Column(db.String(255))
    message = db.Column(db.Text)
