from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin, Page

STYLE_DATA = (
    ("hor-minimalist-a", "Horizontal Minimalist A", False),
    ("hor-minimalist-b", "Horizontal Minimalist B", False),
    ("box-table-a", "Box Table A", False),
    ("box-table-b", "Box Table B", False),
    ("hor-zebra", "Horizontal Zebra", False),
    ("ver-zebra", "Vertical Zebra", True),
    ("one-column-emphasis", "One Column Emphasis", False),
    ("newspaper-a", "Newspaper A", False),
    ("newspaper-b", "Newspaper B", False),
    ("newspaper-c", "Newspaper C", False),
    ("gradient-style", "Gradient Style", False),
    ("pattern-style-a", "Pattern Style A", False),
    ("pattern-style-b", "Pattern Style B", False),
    )

STYLE_CHOICES = [(index, name) for (index, name, js) in STYLE_DATA]
STYLE_JS = dict((index, js) for (index, name, js) in STYLE_DATA)

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

    def js(self):
     return STYLE_JS[self.style]

    def __unicode__(self):
        return self.name


    search_fields = ('name', 'table_data')
