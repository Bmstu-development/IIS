from rest_framework import routers

from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.redirect_from_start_page, name='start_page'),
    path('people/', views.PeopleListView.as_view(), name='people_list'),
    path('people/add', views.PersonAddView.as_view(), name='person_add'),
    path('people/<int:pk>', views.PersonDetailView.as_view(), name='person_detail'),
]

router = routers.DefaultRouter()
router.register(r'people', views.PeopleViewSet)

"""
API URLs:
    /api/v1/people/
    /api/v1/people/<pk>/
    /api/v1/people/<pk>/get_events/
    /api/v1/people/<pk>/get_departments/
"""
urlpatterns += [
    path('api/v1/', include(router.urls))
]
