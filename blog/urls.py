from django.contrib import admin
from django.urls import path,include
from .views import BlogView,IndividualView,NewView,editview,deleteview

urlpatterns = [
    path('',BlogView.as_view(),name="home"),
    path('individual/<int:pk>/',IndividualView.as_view(),name="individual"),
    path ('add/',NewView.as_view(),name="add"),
    path('edit/<int:pk>',editview.as_view(),name='edit'),
     path('delete/<int:pk>',deleteview.as_view(),name='delete'),
    path('accounts/',include('django.contrib.auth.urls'),name="login"),
    
]
