from datetime import date
from django.db import models
from django.core.urlresolvers import reverse

class Article(models.Model):
    name = models.CharField( max_length=255, )
    slug = models.SlugField( unique=True, max_length=255, )
    image = models.ImageField( upload_to="ArticleImages/", blank=True, null=True)
    short_content = models.TextField( blank=True, )
    sort = models.IntegerField( default=0, )
    is_active = models.BooleanField( default=True, )
    meta_description = models.CharField( max_length=255, blank=True, )
    meta_keywords = models.CharField( max_length=255, blank=True, )
    date = models.DateField( default=date.today )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug':self.slug})
        
    class Meta:
        app_label = 'blog'
        ordering = ['sort','name']

class ArticleSection(models.Model):
    article = models.ForeignKey('Article')
    sort = models.IntegerField( default=0, )
    image = models.ImageField( upload_to="ArticleImages/", blank=True, null=True )
    image_caption = models.CharField( max_length=255, null=True, blank=True )
    section_header = models.CharField( max_length=255 )
    article_section = models.TextField()
    
    def __str__(self):
            return '%s, %s' % (self.article, self.section_header)

    class Meta:
        app_label = 'blog'
        ordering = ['sort']
