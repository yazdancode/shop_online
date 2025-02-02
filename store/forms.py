from django import forms
from django.core.validators import RegexValidator
from store.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["phone", "password", "email", "otp_code"]
        labels = {
            "phone": "تلفن همراه",
            "email": "ایمیل",
            "password": "رمز عبور",
        }
        widgets = {
            "phone": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "شماره موبایل یا ایمیل",
                    "style": "direction:ltr; text-align:left; font-family:IRANYekan, sans-serif; font-size:10px; ",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "ایمیل خود را وارد کنید",
                    "style": "direction:ltr; text-align:left; font-family:IRANYekan, sans-serif; font-size:10px; "
                    "text-decoration:none solid rgb(35, 37, 78); word-spacing:0; background-color:#FFFFFF; "
                    "color:#23254E; height:48px; width:334.4px; border:1px solid #D32F2F; padding:8px 0px; "
                    "display: flex; overflow:hidden; cursor:default;",
                    "autocomplete": "email",
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "style": "direction:ltr; text-align:left; font-family:IRANYekan, sans-serif; font-size:10px; "
                    "text-decoration:none solid rgb(35, 37, 78); word-spacing:0; background-color:#FFFFFF; "
                    "color:#23254E; height:48px; width:334.4px; border:1px solid #D32F2F; padding:8px 0px; "
                    "display: flex; overflow:hidden; cursor:default;",
                    "placeholder": "رمز عبور خود را وارد کنید",
                    "autocomplete": "off",
                }
            ),
        }
        validators = {
            "phone": [
                RegexValidator(
                    regex=r"^\d{10,15}$",
                    message="شماره تلفن باید فقط شامل اعداد باشد و بین ۱۰ تا ۱۵ رقم باشد.",
                )
            ]
        }


class VerificationForm(forms.Form):
    code = forms.CharField(label="کد تأیید")
