from django import forms

from personal_info_project.models import Person


class PersonForm(forms.ModelForm):
    class Meta:         #classe interna para configurar o formulário
        model = Person
        fields = ['name','age'] #quais campos do model serão expostos no formulário
        labels = {
            'name': "Nome",
            'age' : "Idade"
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()        #TODO testar
        if name and len(name) < 3:
            raise forms.ValidationError("O nome deve ter pelo menos 3 caracteres.")
        return name

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age > 150:
            raise forms.ValidationError("Insira um valor inferior a 150.")
        elif age <= 0:
            raise forms.ValidationError("Idade inválida. Tente novamente.")
        return age

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})