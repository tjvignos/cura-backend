from django.urls import path
from . import views

circle_list = views.CircleViewSet.as_view({
  'get': 'list',
  'post': 'create',
})

circle = views.CircleViewSet.as_view({
  'get': 'retrieve',
  'put': 'update',
  'delete': 'destroy',
})



urlpatterns = [
  path('', circle_list, name='circle-list'),
  path('<int:pk>/', circle, name='circle'),
  path('<int:pk>/add/<int:user_id>/', views.add_user, name='add-user'),
  path('<int:pk>/remove/<int:user_id>/', views.remove_user, name='remove-user')
]