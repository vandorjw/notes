from django.db import models

class Venue(models.Model):
    name = models.CharField( max_length=255 )
    description = models.TextField()
    url = models.CharField( max_length=255, blank=True )
    image = models.ImageField(upload_to="contact/", blank=True, null=True)
    is_active = models.BooleanField( default=True )
    sort = models.IntegerField( default=0 )

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'contact'
        ordering = ['sort', 'name']
