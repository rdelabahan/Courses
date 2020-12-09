from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('<int:course_id>', views.remove),
    path('<int:course_id>/delete', views.delete),
    path('<int:course_id>/comments', views.comment),
    path('<int:course_id>/add_comment', views.add_comment),
    path('<int:course_id>/<int:comment_id>/delete_comment', views.delete_comment),
    
]