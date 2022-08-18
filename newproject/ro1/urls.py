from django.urls import path 
from . import views

urlpatterns = [
         path('', views.home, name='home'),
         path("create/", views.addFriend,name='create'),
         path("create/detail/<int:id>/", views.friendDetail, name="detail"),
         path('delete/<int:id>/',views.deleteFriend, name='delete'),
         path('edit/<int:id>/',views.editFriend, name="edit"),
        #  path('index/', views.index, name='index'),
         path('index/', views.IndexView.as_view(), name='index'),
        #  path('detail2/<int:question_id>/', views.detail2, name='detail2'),
        path('detail2/<int:pk>/', views.DetailView.as_view(), name='detail2'),
        #  path('result/<int:question_id>/', views.results, name='results'),
        path('result/<int:pk>/', views.ResultsView.as_view(), name='results'),
        path('vote/<int:question_id>/', views.vote, name='vote'),

]