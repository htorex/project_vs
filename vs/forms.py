from django import forms

from users.models import User


class Registerform(forms.Form):
    
    username = forms.CharField(required=True,
                               min_length=6, max_length=50,
                               widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id' : 'username',
                                    'placeholder' : 'Username',
                               }))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={
                                'class': 'form-control',
                                'id' : 'email',
                                'placeholder' : 'example@mail.com',
                             }))
    rut = forms.CharField(required=True,
                               min_length=6, max_length=50,
                               widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id' : 'rut',
                                    'placeholder' : 'Rut solo con -',
                               }))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={
                               'class' : 'form-control',
                               'placeholder' : 'Contraseña',
                               }))
    
    def clean_username(self):

        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('el username ya se encuentra registrado')
        
        return username


    def clean_email(self):

        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('el email ya se encuentra registrado')
        
        return email
    

    def clean_rut(self):

        rut = self.cleaned_data.get('rut')

        if User.objects.filter(rut=rut).exists():
            raise forms.ValidationError('el rut ya se encuentra registrado')
        
        return rut