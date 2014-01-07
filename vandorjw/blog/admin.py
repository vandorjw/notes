from django.contrib import admin
from blog.models import Article, ArticleSection

class ArticleSection_Inline(admin.StackedInline):
    model = ArticleSection
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",),
    }

    list_per_page = 25

    list_display = (
        '__str__',
        'is_active',
        'sort',
    )
    inlines = [ ArticleSection_Inline, ]

admin.site.register(Article, ArticleAdmin)
