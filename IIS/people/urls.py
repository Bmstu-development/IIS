from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirect_from_start_page, name='start_page'),
    path('people/', views.PeopleListView.as_view(), name='people_list'),
    path('people/add', views.PersonAddView.as_view(), name='person_add'),
    path('people/<int:pk>', views.PersonDetailView.as_view(), name='person_detail'),
    path('people/<int:pk>/delete', views.delete_person, name='person_delete'),
    # path('people/<int:pk>/delete_user', views.delete_user, name='person_user_delete'),
    # path('people/<int:pk>/create_user', views.create_user, name='person_user_create'),
]
