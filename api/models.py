from django.db import models

class Source(models.Model):
    url = models.URLField(max_length=300, unique=True)
    visited = models.BooleanField(default=False)

class Paragraph(models.Model):
    text = models.TextField(max_length=2000)
    source = models.ForeignKey('Source', on_delete=models.SET_NULL, null=True)
    
class GeneratedParagraph(models.Model):
    text = models.TextField(max_length=2000)