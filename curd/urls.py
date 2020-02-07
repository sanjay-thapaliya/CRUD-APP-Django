from django.urls import path
from curd import views

urlpatterns = [

    path('', views.LookBlog.as_view(), name='see_blog'),
    path('create/', views.CreateBlog.as_view(), name='create_views'),
    path('delete/<int:pk>', views.DeleteBLog.as_view(), name='delete_views'),
    path('update/<int:pk>', views.UpdateBlog.as_view(), name='update_views'),


]