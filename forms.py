from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired, Length, Email,EqualTo

class RegistrationForm(FlaskForm):
    # in the validators section DataRequired() means it cant be empty
    #length min max is the range of len of the username
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    #for validation of email...call Email()
    email=StringField('Email',validators=[DataRequired(),Email()])
    #for password we use PasswordField
    password=PasswordField('Password',validators=[DataRequired()])
    #here, we call EqualTo method to check if its equal to password entered
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    #call submitfield for submitting
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    
    email=StringField('Email',validators=[DataRequired(),Email()])
    #even if browser closes...this will stay logged in for sometime using a secured cookie
    remember=BooleanField('Remember Me')
    password=PasswordField('Password',validators=[DataRequired()])
     
    submit = SubmitField('Login')

    