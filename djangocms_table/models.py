from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin, Page

STYLE_CHOICES = (
    ("One", "one"),
    ("Two", "Two")
    )

class Table(CMSPlugin):
    """
    Table plugin
    """

    name = models.CharField(_("name"), max_length=256)

    headers_top = models.PositiveSmallIntegerField(_("top"), default=1)
    headers_left = models.PositiveSmallIntegerField(_("left"), default=0)
    headers_bottom = models.PositiveSmallIntegerField(_("bottom"), default=0)
    table_data = models.TextField(_("table data"))
    style = models.CharField("Style", max_length=80, choices=STYLE_CHOICES, null=True)


    def __unicode__(self):
        return self.name


    search_fields = ('name', 'table_data')
