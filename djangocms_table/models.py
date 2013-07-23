from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin, Page

STYLE_CHOICES = (
    ("hor-minimalist-a", "Horizontal Minimalist A"),
    ("hor-minimalist-b", "Horizontal Minimalist B"),
    ("box-table-a", "Box Table A"),
    ("box-table-b", "Box Table B"),
    ("hor-zebra", "Horizontal Zebra"),
    ("ver-zebra", "Vertical Zebra"),
    ("one-column-emphasis", "One Column Emphasis"),
    ("newspaper-a", "Newspaper A"),
    ("newspaper-b", "Newspaper B"),
    ("newspaper-c", "Newspaper C"),
    ("gradient-style", "Gradient Style"),
    ("pattern-style-a", "Pattern Style A"),
    ("pattern-style-b", "Pattern Style B"),
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
