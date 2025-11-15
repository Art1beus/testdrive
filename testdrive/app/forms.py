from django import forms

CARS = ((1, 'Nissan Murano'), (2, 'Lada Vesta'), (3, 'BMW X5'))

class UserForm(forms.Form):
    name = forms.CharField(label='Имя')
    phone = forms.CharField(label='Телефон')
    email = forms.EmailField(label='Почта')
    car = forms.ChoiceField(label='Машина', choices=CARS)
    comment = forms.CharField(label='Комментарий', widget=forms.Textarea)