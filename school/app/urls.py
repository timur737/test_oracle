from django.urls import path
from .views import student_views
from .views.search_views import SearchResultsView
from .views.class_views import ClassCreateView, SchoolCreateView

app_name = 'school'

urlpatterns = [
    path('', student_views.StudentListView.as_view(), name='all'),
    path('student/<int:pk>/detail', student_views.StudentDetailView.as_view(), name='student_detail'),
    path('student/create/', student_views.StudentCreateView.as_view(), name='student_create'),
    path('student/<int:pk>/update/', student_views.StudentUpdateView.as_view(), name='student_update'),
    path('student/<int:pk>/delete/', student_views.StudentDeleteView.as_view(), name='student_delete'),
    path("student/search/", SearchResultsView.as_view(), name="search_results"),
    path('send_email/', student_views.SendMailToStudentView.as_view(), name='send_email'),
    path('message_sent/', student_views.MessageSentView.as_view(), name='message_sent'),
    path('class/create/', ClassCreateView.as_view(), name='create_class'),
    path('school/create/', SchoolCreateView.as_view(), name='create_school'),

]
