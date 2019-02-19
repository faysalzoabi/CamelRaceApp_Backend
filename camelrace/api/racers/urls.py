from django.urls import path
from api.racers.views import RacerListView, RaceCreateView, DetailListView, RaceUpdateView, RaceDeleteView

urlpatterns = [
    path('', RacerListView.as_view(), name='racers'),
    path('create/', RaceCreateView.as_view(), name='createracers'),
    path('<pk>', DetailListView.as_view(), name='view-specificracer'),
    path('<pk>/update/', RaceUpdateView.as_view(), name='update-specificracer'),
    path('<pk>/delete/', RaceDeleteView.as_view(), name='delete-specificracer'),
]
