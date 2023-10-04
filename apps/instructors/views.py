from django.contrib.messages.views import SuccessMessageMixin
from django.forms import widgets
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Instructor


class InstructorListView(ListView):
    model = Instructor


class InstructorDetailView(DetailView):
    model = Instructor
    template_name = "instructors/instructor_detail.html"


class InstructorCreateView(SuccessMessageMixin, CreateView):
    model = Instructor
    fields = "__all__"
    success_message = "New instructor successfully added"

    def get_form(self):
        """add date picker in forms"""
        form = super(InstructorCreateView, self).get_form()
        form.fields["date_of_birth"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["date_of_admission"].widget = widgets.DateInput(
            attrs={"type": "date"}
        )
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 1})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 1})
        return form


class InstructorUpdateView(SuccessMessageMixin, UpdateView):
    model = Instructor
    fields = "__all__"
    success_message = "Record successfully updated."

    def get_form(self):
        """add date picker in forms"""
        form = super(InstructorUpdateView, self).get_form()
        form.fields["date_of_birth"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["date_of_admission"].widget = widgets.DateInput(
            attrs={"type": "date"}
        )
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 1})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 1})
        return form


class InstructorDeleteView(DeleteView):
    model = Instructor
    success_url = reverse_lazy("instructor-list")
