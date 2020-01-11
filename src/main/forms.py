from django import forms
from .models import ContactUser, SubscribeUser

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        max_length=40,
        required=True,
        widget=forms.TextInput(attrs={'class': '',
                                       'placeholder': '',
                                       'id': 'name',
                                       'type': 'text',
                                       'name': 'name'}
                               )
    )
    email = forms.EmailField(
        required=True,
        max_length=120,
        widget=forms.EmailInput(attrs={'class': '',
                                       'placeholder': '',
                                       'id': 'email',
                                       'type': 'email',
                                       'name': 'email'}
        )
    )
    message = forms.CharField(
        required=True,
        max_length=240,
        widget=forms.Textarea(attrs={'class': '',
                                       'placeholder': '',
                                       'id': 'message',
                                       'type': 'text',
                                       'rows': '6',
                                       'name': 'message'}
        )
    )

    class Meta:
        model = ContactUser
        fields = ('name', 'email', 'message',)


class SubscribeForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        max_length=120,
        widget=forms.EmailInput(attrs={'class': '',
                                       'placeholder': 'Email Address',
                                       'id': 'email',
                                       'type': 'email',
                                       'name': 'email'}
        )
    )

    class Meta:
        model = SubscribeUser
        fields = ('email',)


    """def save(self, commit=True):
        user = super(ContactForm, self).save(commit=False)
        user.name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']
        user.message = self.cleaned_data['message']
        if commit:
            user.save()

        return user"""
