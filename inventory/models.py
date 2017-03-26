from __future__ import unicode_literals

from django.db import models

class Item(models.Model):
	title = models.CharField(max_length=300)
	description = models.TextField(blank=True, null=True)
	amount = models.IntegerField()
	barcode = models.CharField(max_length=100, blank=True, null=True)
