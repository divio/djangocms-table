import json

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

from .forms import TableForm
from .models import Table
from .utils import static_url


class TablePlugin(CMSPluginBase):
    model = Table
    form = TableForm
    name = _("Table")
    render_template = "cms/plugins/table.html"
    text_enabled = True

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        (_('Headers'), {

            'fields': (('headers_top', 'headers_left', 'headers_bottom'),)
        }),
        (None, {
            'fields': ('table_data', 'csv_upload')
        })
    )

    def render(self, context, instance, placeholder):
        try:
            data = json.loads(instance.table_data)
        except:
            data = "error"
        context.update({
            'name': instance.name,
            'data': data,
            'instance':instance,
        })
        return context

    def icon_src(self, instance):
        return static_url("img/table.png")

    def response_change(self, request, obj):
        response = super(TablePlugin, self).response_change(request, obj)
        if 'csv_upload' in request.FILES.keys():
            self.object_successfully_changed = False
        return response

plugin_pool.register_plugin(TablePlugin)
