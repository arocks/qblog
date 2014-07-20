from django.views import generic
from . import models


class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 2


class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"


class TagDetail(generic.DetailView):
    model = models.Tag
    template_name = "tag.html"
    slug_url_kwarg = "tag"
