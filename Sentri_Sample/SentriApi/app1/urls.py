from django.urls import path
from .views import EmissionsListCreate, EmissionsDetail

urlpatterns = [
    path('emissions/', EmissionsListCreate.as_view(),
         name='emissions-list-create'),

    path('emissions/<int:pk>/', EmissionsDetail.as_view(),
         name='emissions-detail'),  # x new line

]
