from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('readNotice/', views.readNotice),
    path('readNotice/<int:notice_id>/', views.detail),
    path('readNotice/create/', views.create),
    path('createNotice/', views.createNotice),
    path('readNotice/<int:notice_id>/update/delete/', views.delete),
    path('readNotice/<int:notice_id>/update/', views.update),
    path('readNotice/<int:notice_id>/update/update_notice/', views.update_notice),
]
