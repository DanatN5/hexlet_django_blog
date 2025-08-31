from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

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
        context = {"name": "article"},
        return render(request, "index.html", context)

