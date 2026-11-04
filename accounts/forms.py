"""Formularios con reCAPTCHA (Fase 2, RNF03)."""

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class RegistroForm(UserCreationForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())


class LoginForm(AuthenticationForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
