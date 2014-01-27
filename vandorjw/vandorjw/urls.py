from django.conf.urls import patterns, include, url
from django.contrib import admin
from .sitemap import BlogSitemap
from .views import RobotPageView, HumanPageView, GooglePageView
admin.autodiscover()

sitemaps = {
    'blog': BlogSitemap,
}

urlpatterns = patterns('',
    url(
        regex=r"^robots\.txt$",
        view=RobotPageView.as_view(),
        name="site_robots",
    ),
    url(
        regex=r"^humans\.txt$",
        view=HumanPageView.as_view(),
        name="site_humans",
    ),
    url(
        regex=r"^google25e8e23e2bfc7d2c\.html$",
        view=GooglePageView.as_view(),
        name="google_webmasters",
    ),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^browserid/', include('django_browserid.urls')),
    url(r"^contact/$", include('contact.urls', namespace='contact', app_name='contact')),
    url(r"^", include('blog.urls', namespace='blog', app_name='blog')),
)
