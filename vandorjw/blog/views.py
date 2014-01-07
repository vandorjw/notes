from django.views import generic
from blog.models import Article

class ArticleDetailView(generic.DetailView):
    model = Article
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['sections'] = self.object.articlesection_set.all()
        return context
    

class ArticleListView(generic.ListView):
    model = Article
    queryset = Article.objects.filter(is_active=True)
