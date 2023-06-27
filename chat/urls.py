from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chats),
    path('chat/<int:id>', views.chat_by_id),
    path('chat/<int:id>/messages', views.messages),
]