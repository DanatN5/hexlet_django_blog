from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import View, TemplateView
from django.urls import reverse

'''
def index(request):
    return render(
        request,
        "index.html",
        context={
            "name": "article",
        },
    )
'''

class IndexView(View):
    def get(self, request):
        context = {"article_id": 42, "tags": "python"}
        return redirect(reverse("Tags", kwargs=context))
    
class TagsView(TemplateView):
    template_name = "articles/tags.html"

    def get(self, request, article_id, tags):
        return render(
            request,
            self.template_name,
            context={"article_id": article_id, "tags": tags},
        )

