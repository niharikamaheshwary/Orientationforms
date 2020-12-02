from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import Snippet


class ContactForm(forms.Form):
    name = forms.CharField()
    rno = forms.IntegerField(label='Roll-Number')
    q1 = forms.CharField(widget=forms.Textarea, label='If you had an invisibility cloak, what would you do?')
    q2 = forms.CharField(widget=forms.Textarea, label='You find a couple making out in TL, what do you do?')
    q3 = forms.CharField(widget=forms.Textarea, label='Where is the IITB chamber of secrets?')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout= Layout(
            'name',
            'rno',
            'q1',
            'q2',
            'q3',
            Submit('submit', 'Submit', css_class='btn-success')
        )





class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('name', 'rno','q1','q2','q3')
