from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length

##WTForm


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=64)])
    role = SelectField(choices=["admin", "tester", "user"], validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


class EditForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=64)])
    role = SelectField(choices=["admin", "tester", "user"], validators=[DataRequired()])
    submit = SubmitField("Edit me!")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")

