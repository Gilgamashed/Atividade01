from django import forms

from personal_info_project.models import Person, ContactLog
from .constants import GENDER_OPTIONS


class PersonForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=GENDER_OPTIONS,
        initial='U',
    )

    class Meta:         #classe interna para configurar o formulário
        model = Person
        fields = ['name','age','gender'] #quais campos do model serão expostos no formulário
        labels = {
            'name': "Nome",
            'age' : "Idade",
            'gender': "Gênero"
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
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


class FeedbackForm(forms.Form):
    name = forms.CharField(label="Seu nome", max_length=100)
    email = forms.EmailField(label="E-mail")
    message = forms.CharField(label="Comentário", widget=forms.Textarea)
    rating = forms.ChoiceField(label="Avaliação",
                               choices=[
                                   ('excelente',"Excelente"),
                                   ("bom","Bom"),
                                   ('regular',"Regular"),
                                   ('ruim',"Ruim")
                               ],
                                widget=forms.RadioSelect,)

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if name and len(name) < 3:
            raise forms.ValidationError("Por favor insira um nome com pelo menos 3 caracteres.")
        return name


"""class ContactLogForm(forms.Form):
    person = forms.CharField(label="Seu nome", max_length=100)
    message = forms.CharField(label="Mensagem", widget=forms.Textarea)

    def clean_person(self):
        name = self.cleaned_data['person'].strip()
        if len(name) < 3:
            raise forms.ValidationError("Por favor insira um nome com pelo menos 3 caracteres.")

        try:
            return Person.objects.get(name__iexact=name)
        except Person.DoesNotExist:
            raise forms.ValidationError("Pessoa não encontrada. Verifique o nome ou cadastre-se primeiro.")
-Parecido com o excel, mas o DJango tem um model form próprio que funciona bem com o ForeignKey! 
            """

class ContactLogForm(forms.ModelForm):
    class Meta:
        model = ContactLog
        fields = ['person', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'person': "Nome:",
            'message': "Mensagem:"
        }


