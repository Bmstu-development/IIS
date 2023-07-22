from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirect_from_start_page, name='start_page'),
    path('people/', views.PeopleListView.as_view(), name='people_list'),
    path('people/add', views.PersonAddView.as_view(), name='person_add'),
    path('people/<int:pk>', views.PersonDetailView.as_view(), name='person_detail'),
    # path('people/<int:pk>/delete', views.PersonDeleteView.as_view(), name='person_delete'),
]
