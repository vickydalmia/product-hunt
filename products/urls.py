from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name="products"),
    path('create/', views.create, name="createproduct"),
    path('<int:product_id>/', views.detail, name="details"),
    path('<int:product_id>/upvote/', views.upvote, name="upvote"),
]