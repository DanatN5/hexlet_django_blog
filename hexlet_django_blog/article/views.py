from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.base import View, TemplateView
from django.urls import reverse
from .models import Article, ArticleComment
from .forms import CommentArticleForm, ArticleForm
from django.contrib import messages


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
    
    def post(self, request, *args, **kwargs):
        form = CommentArticleForm(request.POST)
        if form.is_valid():
            comment = ArticleComment(
                content = form.cleaned_data[
                "content"
                ],
            )
            comment.save()


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, "articles/create.html", {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            messages.success(request, "Статья успешно добавлена")
            form.save()
            return redirect('articles')
        
        messages.error(request, "Не удалось добавить статью")
        
        return render(request, 'articles/create.html', {'form': form})
    

class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(
            request,
            "articles/update.html",
            {"form": form,
             "article_id": article_id},
        )
    
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("articles")
        
        return render(
            request,
            "articles/update.html",
            {"form": form,
             "article_id": article_id},
        )
    
class ArticleFormDeleteView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(
            request,
            "articles/delete.html",
            {"form": form,
             "article_id": article_id},
        )


    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect("articles")


        

class TagsView(TemplateView):
    template_name = "articles/tags.html"

    def get(self, request, article_id, tags):
        return render(
            request,
            self.template_name,
            context={"article_id": article_id, "tags": tags},
        )
    


