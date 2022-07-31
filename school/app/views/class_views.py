from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from app.forms import ClassCreateForm, SchoolCreateForm
from app.models import Class, School


class ClassCreateView(LoginRequiredMixin, CreateView):
    """View to create a new class"""
    template_name = 'class/create_class.html'
    form_class = ClassCreateForm
    model = Class
    success_url = reverse_lazy('school:all')


class SchoolCreateView(LoginRequiredMixin, CreateView):
    """View to create a new school"""
    template_name = 'school/create_school.html'
    form_class = SchoolCreateForm
    model = School
    success_url = reverse_lazy('school:all')
