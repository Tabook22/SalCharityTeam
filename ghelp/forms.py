from django import forms
from django.urls import reverse
from .models import Person, Charityapp, Charityappfiels
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field, HTML, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django_countries.widgets import CountrySelectWidget

class addNewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(addNewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_show_labels = True
        # self.helper.layout = Layout(
        #     Row(
        #         Column('sr_org', css_class='form-group col-md-12 mb-0'),
        #         css_class='form-row'
        #     ),
        #     Row(
        #         Column('sr_loc', css_class='form-group col-md-12 mb-0'),
        #         css_class='form-row'
        #     ),
        #     Row(
        #         Column('sr_ser', css_class='form-group col-md-6 mb-0'),
        #         Column('sr_status', css_class='form-group col-md-6 mb-0'),
        #         css_class='form-row'
        #     ),
        #     Row(
        #         Column('sr_order', css_class='form-group col-md-12 mb-0'),
        #         css_class='form-row'
        #     ),
        #     # Row(
        #     #     Column('un',css_class='form-group col-md-12 mb-0'),
        #     #     css_class='form-row'
        #     # ),
        #     Submit('submit', 'Add area(s) of experties')
        # )

    class Meta:
        model = Person
        fields = [
            'name',
            'nationality',
            'cardid',
            'uploadImg',
            'helptype',
            'comments',
        ]
        widgets ={
            'nationality': CountrySelectWidget(),
            'comments':forms.Textarea(attrs={'col':'40','row':'10','class': 'form-control','dir':'rtl'}),
        }


class CharityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CharityForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_show_labels = True
    class Meta:
        model = Charityapp
        fields = [
            'name',
            'tel',
            'health',
            'debt',
            'housing',
            'totalicone',
            'familyno',
            'soc',
            'Helptype',
        ]



class CharityappfielsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CharityappfielsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_show_labels = True
    class Meta:
        model = Charityappfiels
        fields = [
        'upload_1',
        'upload_2',
        'upload_3',
        'upload_4',
        'upload_5',
        'upload_6',
        'upload_7',
        'upload_8',
        'upload_9',
        'upload_10',
        ]
        widgets={
        'upload_1':forms.ClearableFileInput(attrs={'multiple': True}),
        'upload_2':forms.ClearableFileInput(attrs={'multiple': True}),
        'upload_3':forms.ClearableFileInput(attrs={'multiple': True}),
        'upload_4':forms.ClearableFileInput(attrs={'multiple': True}),
        'upload_5':forms.ClearableFileInput(attrs={'multiple': True}),
        'upload_6':forms.ClearableFileInput(attrs={'multiple': True}),
        'upload_7':forms.ClearableFileInput(attrs={'multiple': True}),
        'upload_8':forms.ClearableFileInput(attrs={'multiple': True}),
        'upload_9':forms.ClearableFileInput(attrs={'multiple': True}),
        'upload_10':forms.ClearableFileInput(attrs={'multiple': True}),
        }





