from django.forms import ModelForm
from .models import Comentario
# from django.forms.widgets import TextInput, EmailInput, Textarea
import requests


class FormComentario(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.label_suffix = ""  # Para tirar : depois do nome

    def clean(self):
        raw_data = self.data

        recaptcha_response = raw_data.get('g-recaptcha-response')

        # if not recaptcha_response:
        #     self.add_error(
        #         'comentario',
        #         'Por favor, marque a caixa "Não sou um robô".'
        #     )

        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': '6LdYiLoZAAAAANrov4M0h2MSEQvjnZeV0sm4NgXh',
                'response': recaptcha_response
            }
        )
        recaptcha_result = recaptcha_request.json()

        if not recaptcha_result.get('success'):
            self.add_error(
                'comentario',
                'Desculpe Mr. Robot, ocorreu um erro.'
            )

        cleaned_data = self.cleaned_data
        nome = cleaned_data.get('nome_comentario')
        email = cleaned_data.get('email_comentario')
        comentario = cleaned_data.get('comentario')

        if len(nome) < 5:
            self.add_error(
                'nome_comentario',
                'Nome precisa ter mais que 5 caracteres.'
            )

    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')
        # labels = { # Não precisa por conta do verbose
        #     'nome': 'Nome',
        #     'descricao': 'Descrição',
        # }
        # widgets = {
        #     'nome_comentario': TextInput(attrs={
        #         'placeholder': 'Digite seu nome',
        #         'class': 'form-control',
        #     }),
        #     'email_comentario': EmailInput(attrs={
        #         'placeholder': 'Digite seu e-mail',
        #         'class': 'form-control',
        #     }),
        #     'comentario': Textarea(attrs={
        #         'placeholder': 'Digite seu cometário',
        #         'class': 'form-control',
        #         # 'rows': 5,
        #     }),
        # }
