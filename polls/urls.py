from django.urls import path, include
from polls import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:x>/', views.detail_sunhan, name="detail_sunhan"),
    path('where/all', views.where, name="where"),
    path('where/<int:x>', views.where_detail, name="where_detail"),
    path('analy/', views.analy, name="analy"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('aboutus/detail', views.aboutusdetail, name="aboutusdetail"),
]
