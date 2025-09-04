from django.shortcuts import render, redirect, get_object_or_404
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
    

class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(
            request,
            "articles/show.html",
            context={
                "article": article,
            },
        )
    

class ArticleCommentsView(View):
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=kwargs["id"], article_id=kwargs["article_id"])
        return render(
            request,
            "articles/show.html",
             context={
                 "comment": comment,
             }
        )
    
class TagsView(TemplateView):
    template_name = "articles/tags.html"

    def get(self, request, article_id, tags):
        return render(
            request,
            self.template_name,
            context={"article_id": article_id, "tags": tags},
        )
    


