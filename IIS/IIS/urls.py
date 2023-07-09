"""
URL configuration for IIS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import routers

from django.contrib import admin
from django.urls import path, include

from people import api_views as people_api
from events import api_views as events_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('people.urls')),
    path('events/', include('events.urls')),
    path('departments/', include('departments.urls')),
]

router = routers.DefaultRouter()

router.register(r'people', people_api.PeopleViewSet)
router.register(r'events', events_api.EventsViewSet)

"""
People API URLs:
    /api/v1/people/
    /api/v1/people/<pk>/
    /api/v1/people/<pk>/get_events/
    /api/v1/people/<pk>/get_departments/
Events API URLs:
    /api/v1/events/
    /api/v1/events/<pk>/
"""
urlpatterns += [
    path('api/v1/', include(router.urls))
]
