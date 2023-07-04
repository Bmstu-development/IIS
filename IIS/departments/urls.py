from django.urls import path

from . import views

urlpatterns = [
    path('departments', views.DepartmentsListView.as_view(), name='departments_list'),
    path('departments/add', views.DepartmentAddView.as_view(), name='departments_add'),
    path('departments/<int:pk>', views.DepartmentDetailView.as_view(), name='departments_detail'),
]
