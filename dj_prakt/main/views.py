from django.shortcuts import render
from django.views.generic.base import ContextMixin
from django.views.generic.base import TemplateView


class CategoryListMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(CategoryListMixin, self).get_context_data(**kwargs)
        context["current_url"] = self.request.path
        return context


class MainPageView(TemplateView, CategoryListMixin):
    template_name = "main/main.html"


def main_view(request):
    title = "Darkfree"
    content = "Hello World!"
    return render(request, 'index.html', {'title': title, 'content': content})
