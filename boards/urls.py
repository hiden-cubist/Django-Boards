from django.urls import path

from . import views

app_name = 'boards'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:board_pk>/', views.board_topics, name='board_topics'),
    path('<int:board_pk>/new/', views.new_topic, name='new_topic'),
    path('<int:board_pk>/topics/<int:topic_pk>/', views.topic_posts, name='topic_posts'),
    path('<int:board_pk>/topics/<int:topic_pk>/reply/', views.reply_topic, name='reply_topic'),
]
