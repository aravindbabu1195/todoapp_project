from django.urls import path
from todoapp import views

urlpatterns = [

    path('', views.add, name='add'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('listview/', views.Tasklistview.as_view(), name='listview'),
    path('detailview/<int:pk>/', views.Taskdetailview.as_view(), name='detailview'),
    path('updateview/<int:pk>/', views.Taskupdateview.as_view(), name='updateview'),
    path('deleteview/<int:pk>/', views.Taskdeleteview.as_view(), name='deleteview'),
]
