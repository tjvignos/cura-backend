from django.urls import path
from . import views

checkin_list = views.CheckinViewSet.as_view({
  'get': 'list',
  'post': 'create',
})

checkin = views.CheckinViewSet.as_view({
  'get': 'retrieve',
  'put': 'update',
  'delete': 'destroy',
})

urlpatterns = [
  path('', checkin_list, name='checkin-list'),
  path('<int:pk>/', checkin, name='checkin'),
]