from django import forms
from django.db import models
from django.forms import ModelForm, MultipleChoiceField
from django.forms.widgets import Textarea
from django.utils.text import capfirst
from django.core import exceptions
from datetime import datetime

# Form Field classes: via http://djangosnippets.org/snippets/2753/

class MultiSelectFormField(forms.MultipleChoiceField):
    widget = forms.CheckboxSelectMultiple
 
    def __init__(self, *args, **kwargs):
        self.max_choices = kwargs.pop('max_choices', 0)
        super(MultiSelectFormField, self).__init__(*args, **kwargs)
 
    def clean(self, value):
        if not value and self.required:
            raise forms.ValidationError(self.error_messages['required'])
        # if value and self.max_choices and len(value) > self.max_choices:
        #     raise forms.ValidationError('You must select a maximum of %s choice%s.'
        #             % (apnumber(self.max_choices), pluralize(self.max_choices)))
        return value

 
class MultiSelectField(models.Field):
    __metaclass__ = models.SubfieldBase
 
    def get_internal_type(self):
        return "CharField"
 
    def get_choices_default(self):
        return self.get_choices(include_blank=False)
 
    def _get_FIELD_display(self, field):
        value = getattr(self, field.attname)
        choicedict = dict(field.choices)
 
    def formfield(self, **kwargs):
        # don't call super, as that overrides default widget if it has choices
        defaults = {'required': not self.blank, 'label': capfirst(self.verbose_name),
                    'help_text': self.help_text, 'choices': self.choices}
        if self.has_default():
            defaults['initial'] = self.get_default()
        defaults.update(kwargs)
        return MultiSelectFormField(**defaults)

    def get_prep_value(self, value):
        return value

    def get_db_prep_value(self, value, connection=None, prepared=False):
        if isinstance(value, basestring):
            return value
        elif isinstance(value, list):
            return ",".join(value)
 
    def to_python(self, value):
        if value is not None:
            return value if isinstance(value, list) else value.split(',')
        return ''

    def contribute_to_class(self, cls, name):
        super(MultiSelectField, self).contribute_to_class(cls, name)
        if self.choices:
            func = lambda self, fieldname = name, choicedict = dict(self.choices): ",".join([choicedict.get(value, value) for value in getattr(self, fieldname)])
            setattr(cls, 'get_%s_display' % self.name, func)
 
    def validate(self, value, model_instance):
        arr_choices = self.get_choices_selected(self.get_choices_default())
        for opt_select in value:
            if (opt_select not in arr_choices):  # add int() wrapper around opt_select for comparing with integer choices
                raise exceptions.ValidationError(self.error_messages['invalid_choice'] % value)  
        return
 
    def get_choices_selected(self, arr_choices=''):
        if not arr_choices:
            return False
        list = []
        for choice_selected in arr_choices:
            list.append(choice_selected[0])
        return list
 
    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)




# Actual site models:

LOGO_TYPES = (
	('UID', 'Unit Identifier'),
	('MUID', 'Monogram Unit Identifier'),
	('VUID', 'Vertical Unit Identifier'),
)

class Submission(models.Model):
	unit_name = models.CharField("Unit Name", max_length=300)
	requester = models.CharField("Requested By", max_length=300)
	phone = models.CharField("Phone Number", max_length=50)
	email = models.EmailField(max_length=254)
	department = models.CharField(max_length=300)
	request_date = models.DateTimeField("Requested On", default=datetime.now)
	design_options = MultiSelectField(max_length=250, choices=LOGO_TYPES)
	comments = models.TextField(blank=True)
	def __unicode__(self):
		return self.unit_name
		

class SubmissionForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(SubmissionForm, self).__init__(*args, **kwargs)
		self.fields['requester'].label = 'Your Name'
		self.fields['department'].label = 'Your Department/Office/College'
		self.fields['comments'].label = 'Questions or Comments'
	
	class Meta:
		model = Submission
		fields = ['unit_name', 'requester', 'phone', 'email', 'department', 'design_options', 'comments']