"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional


class SignupForm(FlaskForm):
    # User Sign-up Form

    name = StringField("姓名", validators=[DataRequired()])
    email = StringField(
        "Email",
        validators=[
            Length(min=6),
            Email(message="Enter a valid email."),
            DataRequired(),
        ],
    )
    password = PasswordField(
        "密碼",
        validators=[
            DataRequired(),
            Length(min=6, message="Select a stronger password."),
        ],
    )
    confirm = PasswordField(
        "再次確認密碼",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )
    address = StringField("地址", validators=[Optional()])
    submit = SubmitField("註冊")


class LoginForm(FlaskForm):
    # User Log-in Form

    email = StringField(
        "Email", validators=[DataRequired(), Email(message="輸入email.")]
    )
    password = PasswordField("密碼", validators=[DataRequired()])
    submit = SubmitField("登入")