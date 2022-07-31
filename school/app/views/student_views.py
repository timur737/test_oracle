from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView

from app.forms import SendEmailForm
from app.models import Student


class StudentBaseView(View):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('school:all')
    login_url = 'teacher/login/'


class StudentListView(LoginRequiredMixin, StudentBaseView, ListView):
    """View to list all films.
    Use the 'film_list' variable in the template
    to access all Film objects"""
    template_name = 'students/student_list.html'
    # redirect_field_name = 'redirect_to'


class StudentDetailView(LoginRequiredMixin, StudentBaseView, DetailView):
    """View to list the details from one student.
    Use the 'student' variable in the template to access
    the specific student here and in the Views below"""
    template_name = 'students/student_detail.html'


class StudentCreateView(LoginRequiredMixin, StudentBaseView, CreateView):
    """View to create a new student"""
    template_name = 'students/student_form.html'


class StudentUpdateView(LoginRequiredMixin, StudentBaseView, UpdateView):
    """View to update a student"""
    template_name = 'students/student_form.html'


class StudentDeleteView(LoginRequiredMixin, StudentBaseView, DeleteView):
    """View to delete a student"""
    template_name = 'students/student_confirm_delete.html'


class SendMailToStudentView(LoginRequiredMixin, FormView):
    form_class = SendEmailForm
    template_name = 'students/send_email_form.html'
    success_url = '/message_sent/'

    def form_valid(self, form):
        students = Student.objects.all().values_list('email', flat=True)
        try:
            send_mail(
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[*students]
            )
        except Exception as e:
            raise Exception(e)
        return super(SendMailToStudentView, self).form_valid(form)


class MessageSentView(LoginRequiredMixin, TemplateView):
    template_name = 'students/email_sent.html'
