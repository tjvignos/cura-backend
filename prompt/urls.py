from django.urls import path
from . import views

prompt_list = views.PromptViewSet.as_view({
  'get': 'list',
  'post': 'create',
})

prompt = views.PromptViewSet.as_view({
  'get': 'retrieve',
  'put': 'update',
  'delete': 'destroy',
})

urlpatterns = [
  path('', prompt_list, name='prompt-list'),
  path('<int:pk>/', prompt, name='prompt'),
]