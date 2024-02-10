from django.urls import path
from . import views

urlpatterns = [
    path('Slist/', views.ListCreateAPIView.as_view()),
    path('Mlist/', views.ListMCreateAPIView.as_view()),
    path('NSens/', views.CreateSAPIView.as_view()),
    path('USens/', views.RetrieveUpdateAPIView.as_view()),
    path('NMeasure/', views.CreateMAPIView.as_view())
]
