from django.urls import path

from . import views

urlpatterns = [
    path('', views.DepartmentsListView.as_view(), name='departments_list'),
    path('add', views.DepartmentAddView.as_view(), name='departments_add'),
    path('<int:pk>', views.DepartmentDetailView.as_view(), name='departments_detail'),
]
