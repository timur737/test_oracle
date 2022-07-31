from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from app.models import Teacher, Class, School


class TeacherRegistrationForm(forms.ModelForm):
    error_messages = {
        "password_mismatch": "The two password fields didn’t match.",
    }
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = Teacher
        fields = ('phone_number', 'subject_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "autofocus"
            ] = True

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password2", error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class SendEmailForm(forms.Form):
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True)


class ClassCreateForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = '__all__'


class SchoolCreateForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'
