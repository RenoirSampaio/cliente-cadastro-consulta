from django import forms
from .models import Customer

class DateInput(forms.DateInput):
    input_type = "date"

class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Nome",
        error_messages={"max_length": "Nome não pode ter mais de 30 caracteres"}
    )

    last_name = forms.CharField(
        label="Sobrenome",
        error_messages={"max_length": "Sobrenome não pode ter mais de 30 caracteres"}
    )

    email = forms.EmailField(
        label="E-mail",
        error_messages={"max_length": "Email não pode ter mais de 250 caracteres"}
    )

    birth_date = forms.DateField(label="Data de Nascimento", widget=DateInput())

    area_code = forms.RegexField(
        label="DDD",
        regex=r"^\+?1?[0-9]{2}$",
        error_messages={"invalid": "Número de DDD inválido"}
    )

    phone_number = forms.RegexField(
        label="Telefone",
        regex=r"^\+?1?[0-9]{9,15}$",
        error_messages={"invalid": "Número de telefone inválido"}
    )

    country = forms.CharField(label="País", 
        error_messages={"max_length": "País não pode ter mais de 30 caracteres"}
    )

    state = forms.CharField(label="Estado",
        error_messages={"max_length": "Estado não pode ter mais de 30 caracteres"}
    )

    city = forms.CharField(label="Cidade",
        error_messages={"max_length": "Cidade não pode ter mais de 30 caracteres"}
    )

    buy_date = forms.DateField(label="Data da Compra", widget=DateInput())

    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "email",
            "birth_date",
            "area_code",
            "phone_number",
            "country",
            "state",
            "city",
            "buy_date",
        )