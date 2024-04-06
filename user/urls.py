from django.urls import path
from . import views
from .views import UserViewSet

user_list = UserViewSet.as_view({
  'get': 'list',
})

user = UserViewSet.as_view({
  'get': 'retrieve',
  'put': 'update',
  'delete': 'destroy',
})

urlpatterns = [
  path('', user_list, name='user-list'),
  path('<int:pk>/', user, name='user'),
  path('register/', views.register, name='register'),
  path('login/', views.login, name='login'),
  path('test_token/', views.test_token, name='test_token'),
  path('<int:pk>/circles/', views.circles, name='circles'),
  path('<int:pk>/checkin/', views.checkin, name='checkin'),
  path('<int:pk>/<int:sk>/mutualcircles/', views.mutualcircles, name='mutualcircles'),
]