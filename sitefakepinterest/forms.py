# Criar os formulários do nosso site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from sitefakepinterest.models import Usuario


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    botao_submit_login = SubmitField('Fazer Login')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError('Usuário inexistente. Crie uma conta.')


class FormCriarConta(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    senha = PasswordField('Senha (6 a 20 caracteres)', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação de Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Faça login para continuar.')

    def validate_username(self, username):
        usuario = Usuario.query.filter_by(username=username.data).first()
        if usuario:
            raise ValidationError('Nome de usuário já cadastrado. Escolha outro para continuar.')


class FormFoto(FlaskForm):
    foto = FileField('Foto', validators=[DataRequired()])
    botao_submit_foto = SubmitField('Enviar')
