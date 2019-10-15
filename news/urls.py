from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "news"
urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add_post, name="add"),
    path('save/', views.save_vews, name="save"),
    path('email/', views.email_view, name="email"),
    path('process_email/', views.process_email, name="process"),
]
