from django import forms

from contact_module.models import ContactUs


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'title', 'message')
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'message': forms.Textarea(attrs={'class':'form-control',
                'rows': 5,
                'id': 'message'}),
        }
        labels={
            'name':'نام و نام خانوادگی شما',
            'email':'ایمیل'
        }
        error_messages = {
            'name': {
                'required': 'نام و نام خانوادگی اجباری می باشد. لطفا وارد کنید'
            }
        }