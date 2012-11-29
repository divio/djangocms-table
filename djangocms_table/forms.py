
from django import forms
from django.forms.models import ModelForm
from djangocms_table.widgets import TableWidget
from djangocms_table.models import Table
from django.utils.translation import ugettext_lazy as _


class TableForm(ModelForm):
    table_data = forms.CharField(widget=TableWidget)
    #csv = forms.FileField(label=_("upload .csv file"), help_text=_("upload a .csv file to fill the table up."))
    class Meta:
        model = Table
        exclude = (
            'page',
            'position',
            'placeholder',
            'language',
            'plugin_type',
        )
