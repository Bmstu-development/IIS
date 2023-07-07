from django.urls import path

from . import views


urlpatterns = [
    path('', views.EventsListView.as_view(), name='events_list'),
    path('add', views.EventAddView.as_view(), name='event_add'),
    path('<int:pk>', views.EventDetailView.as_view(), name='event_detail'),
]
