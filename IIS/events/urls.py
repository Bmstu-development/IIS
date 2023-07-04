from django.urls import path

from . import views


urlpatterns = [
    path('events', views.EventsListView.as_view(), name='events_list'),
    path('events/add', views.EventAddView.as_view(), name='event_add'),
    path('events/<int:pk>', views.EventDetailView.as_view(), name='event_detail'),
]
