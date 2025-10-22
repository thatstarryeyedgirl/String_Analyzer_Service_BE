from django.urls import path
from .views import CreateStringView, RetrieveStringView, ListStringView, DeleteStringView

urlpatterns = [
    path('create/', CreateStringView.as_view(), name='create'),
    path('retrieve/<str:value>/', RetrieveStringView.as_view(), name='retrieve'),
    path('list/', ListStringView.as_view(), name='list'),
    
    path('delete/<str:value>', DeleteStringView.as_view(), name='delete')
]