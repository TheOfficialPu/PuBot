"""This module contains forms for the public pages
"""
from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField
from wtforms.validators import Required, Email, Length

def get_form_errors(form):
    """returns the list of reasons the form failed to validate
    """
    reasons = []
    for key in form.errors.keys():
        for err in form.errors[key]:
            reasons.append(err)
    return reasons

class BetaForm(FlaskForm):
    """Form for signing up for the beta
    """
    email = TextField("Email Address",
                      [Email(message="Not a valid email"),
                       Required(message="Email address missing"),
                       Length(max=255, message="Too long for an email")])

class ContactUsForm(FlaskForm):
    """Form for sending messages
    """
    name = TextField('Name', [Required(message='Name missing')])
    email = TextField('Email Address',
                      [Email(), Required(message='Email address missing')])
    phone = IntegerField('Phone Number')
    subject = TextField('Subject',
                        [Required(message='Subject missing'), Length(max=255)])
    message = TextField('Message', [Required(message='message missing')])
