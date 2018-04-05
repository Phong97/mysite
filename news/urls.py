from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('articles/<int:year>/', views.year_archive, name='articlesyearview'),
    path('articles/<int:year>/<int:month>/', views.month_archive, name='articlesmonthview'),
    path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail, name='articles_detailview'),
]