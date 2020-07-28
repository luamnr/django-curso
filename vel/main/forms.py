
from . import models
from django import forms
from django.contrib.auth.models import User
from django.core import validators


class UserForm(forms.ModelForm):
    # confirm_email = forms.EmailField(max_length=192, required=True, label='Confirme seu email')
    # confirm_pass = forms.CharField(max_length=192, required=True, label='Confirme sua senha', widget=forms.PasswordInput)
    # bot_catcher = forms.CharField(required=False,
    #                               validators=[validators.MaxLengthValidator(0, 'SEM BOTS!')],
    #                               widget=forms.HiddenInput)

    class Meta:
        model = User
        fields = [
            # 'first_name',
            'username',
            'password',
            # 'confirm_pass',
            # 'email',

        ]
        labels = {
            # 'first_name': 'Primeiro nome',
            'username': 'Usuário',
            'password': 'Senha',
        }
        widgets = {
            'password': forms.PasswordInput()

        }
        # help_texts = {
        #     'username': None,
        #     'first_name': 'Opcional'
        # }

    # def clean(self):
    #     if self.cleaned_data['email'] != self.cleaned_data['confirm_email'] or \
    #        self.cleaned_data['password'] != self.cleaned_data['confirm_pass']:
    #
    #         if self.cleaned_data['email'] != self.cleaned_data['confirm_email']:
    #             raise forms.ValidationError('Os emails não coincidem')
    #
    #         elif self.cleaned_data['password'] != self.cleaned_data['confirm_pass']:
    #             raise forms.ValidationError('As senhas não coincidem')
    #
    #         return self.cleaned_data


    # def clean_password(self):
    #     if not self.cleaned_data['password'] == self.cleaned_data['confirm_pass']:
    #         raise forms.ValidationError('As senhas não coincidem')
    #     return self.cleaned_data


# class UserProfForm():



