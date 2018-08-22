from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('codefest/<int:year>/', views.codefest, name='codefest'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('announcements/', views.post_list_view.as_view(), name='announcements'),
    path('announcements/<int:pk>/', views.post_detail_view.as_view(), name='post_detail'),
    path('announcements/<int:pk>/comment/', views.comment_create, name='comment_create'),
]
