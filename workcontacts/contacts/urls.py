from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("new_company", views.new_company, name="new_company"),
    path("<slug:slug>/", views.company_employees, name="company_employees"),
    path("new_employee", views.new_employee, name="new_employee"),
    path("profile/<int:id>", views.profile, name="profile"),
    path("communication/<int:id>/delete", views.delete_communication, name="delete_communication"),
    path("employee/<int:id>/delete", views.delete_employee, name="delete_employee"),
    path("company/<int:id>/delete", views.delete_company, name="delete_company"),
]
