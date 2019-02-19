from django.urls import path
from api.Events.views import EventListView, EventDetailView

urlpatterns = [
    path('', EventListView.as_view(), name='events'),
    path('<pk>', EventDetailView.as_view(), name='view_specific_event'),
]
