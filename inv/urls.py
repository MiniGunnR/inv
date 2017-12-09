from django.urls import path

from . import views

urlpatterns = [
    path('lc/create/', views.LCCreateView.as_view(), name='lc_createview'),
]
