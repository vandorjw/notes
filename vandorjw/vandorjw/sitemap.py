from django.contrib.sitemaps import Sitemap
from blog.models import Article

class BlogSitemap(Sitemap):

    def items(self):
        return Article.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.date

