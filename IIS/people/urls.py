from django.urls import path

from . import views
from accounts.views import StartPageView

urlpatterns = [
    path('', StartPageView.as_view(), name='start_page'),
    path('people', views.PeopleListView.as_view(), name='people_list'),
    path('people/add', views.PersonAddView.as_view(), name='person_add'),
    path('people/<int:pk>', views.PersonDetailView.as_view(), name='person_detail'),
]
