from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='chord-home'),
    path('level<int:level>/', views.ChordGenerateView.as_view(), name='get_chord'),
]
