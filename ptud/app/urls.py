from django.urls import path
from . import views

urlpatterns = [
    path('todo1/', views.todo1, name='todo1'),
    path('todo2/', views.todo2, name='todo2'),
    path('cv1/', views.cv1, name='cv1'),
    path('cv2/', views.cv2, name='cv2'),
    path('cv/<str:username>/', views.view_cv, name='view_cv'),
    path('cv_2/<str:username>/', views.cv_2, name='cv_2'),
    path('generate_fake_data/', views.generate_fake_data, name='generate_fake_data'),
    path('add_task/', views.add_task, name='add_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('',views.home, name='home'),
]
