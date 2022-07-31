from django.db.models import Q
from django.views.generic import ListView

from app.models import Student


class SearchResultsView(ListView):
    model = Student
    template_name = "students/search_results.html"
    context_object_name = "object_list"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = None
        if query:
            object_list = Student.objects.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query)
            )
        return object_list
