from django.urls import reverse_lazy
from django.views.generic import CreateView

from app.forms import TeacherRegistrationForm


class SignUp(CreateView):
    form_class = TeacherRegistrationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def post(self, request, *args, **kwargs):
        return super(SignUp, self).post(request, *args, **kwargs)
