from datetime import datetime
from flask import Flask, render_template, flash, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cdgeg'

bootstrap = Bootstrap(app)
moment = Moment(app)

def validate_utoronto_email(form, field):
    if "@utoronto" not in field.data.lower():
        raise ValidationError('Email must be a valid UofT email address')

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    uoft_email = StringField('What is your UofT email address?', validators=[validate_utoronto_email])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        old_email = session.get('uoft_email')
        if old_email is not None and old_email != form.uoft_email.data:
            flash('Looks like you have changed your email!')
        session['name'] = form.name.data
        session['uoft_email'] = form.uoft_email.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), uoft_email=session.get('uoft_email'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)