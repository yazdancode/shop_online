from django import forms
from django.core.validators import RegexValidator
from store.models import Customer


class SearchForm(forms.Form):
    query = forms.CharField(
        label="جستجو",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "عبارت مورد نظر را وارد کنید...",
                "style": "font-family: IRANYekan, sans-serif;",
            }
        ),
    )


class CustomerForm(forms.ModelForm):
    phone = forms.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r"^\d{10,15}$",
                message="شماره تلفن باید فقط شامل اعداد باشد و بین ۱۰ تا ۱۵ رقم باشد.",
            )
        ],
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-sm",
                "placeholder": "شماره تلفن خود را وارد کنید",
                "style": "direction:ltr; text-align:left; font-family:IRANYekan, sans-serif; font-size:10px; "
                "text-decoration:none solid rgb(35, 37, 78); word-spacing:0px; background-color:#FFFFFF; "
                "color:#23254E; height:48px; width:334.4px; border:1px solid #D32F2F; padding:8px 0px; "
                "display: flex; overflow:hidden; cursor:default;",
            }
        ),
    )

    class Meta:
        model = Customer
        fields = ["phone", "password", "email"]
        labels = {
            "phone": "تلفن همراه",
            "email": "ایمیل",
            "password": "رمز عبور",
        }
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "ایمیل خود را وارد کنید",
                    "style": "font-family: IRANYekan, sans-serif;",
                    "autocomplete": "email",
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "رمز عبور خود را وارد کنید",
                    "autocomplete": "off",
                }
            ),
        }
