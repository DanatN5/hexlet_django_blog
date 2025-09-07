from django.urls import path
from hexlet_django_blog.article.views import IndexView, ArticleView, ArticleCommentsView, ArticleFormCreateView

urlpatterns = [
    path("", IndexView.as_view(), name="articles"),
    path("create/", ArticleFormCreateView.as_view(), name="articles_create"),
    path("<int:id>", ArticleView.as_view(), name='articleview'),
    path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view()),
    
]