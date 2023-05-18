from django.urls import path
from .views import AnimeView

urlpatterns = [
    path('anime/', AnimeView.as_view(), name='anime')
]
