from django.urls import path

from . import views

urlpatterns = [
    path('', views.DepartmentsListView.as_view(), name='departments_list'),
    path('add', views.DepartmentAddView.as_view(), name='department_add'),
    path('<int:pk>', views.DepartmentDetailView.as_view(), name='department_detail'),
    path('<int:pk>/delete', views.delete_department, name='department_delete'),
]
