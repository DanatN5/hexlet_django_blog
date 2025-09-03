from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import View, TemplateView
from django.urls import reverse
from .models import Article


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles,
            },
        )
    
class TagsView(TemplateView):
    template_name = "articles/tags.html"

    def get(self, request, article_id, tags):
        return render(
            request,
            self.template_name,
            context={"article_id": article_id, "tags": tags},
        )

