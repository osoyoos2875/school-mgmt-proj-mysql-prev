from django.urls import path

from .views import (
    InstructorCreateView,
    InstructorDeleteView,
    InstructorDetailView,
    InstructorListView,
    InstructorUpdateView,
)

urlpatterns = [
    path("list/", InstructorListView.as_view(), name="instructor-list"),
    path("<int:pk>/", InstructorDetailView.as_view(), name="instructor-detail"),
    path("create/", InstructorCreateView.as_view(), name="instructor-create"),
    path("<int:pk>/update/", InstructorUpdateView.as_view(), name="instructor-update"),
    path("<int:pk>/delete/", InstructorDeleteView.as_view(), name="instructor-delete"),
]
