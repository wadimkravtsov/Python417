from .models import Project
from django.db.models import Q

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginate_projects(request, pr, result):
    page = request.GET.get("page")
    # result = 3
    paginator = Paginator(pr, result)

    try:
        pr = paginator.page(page)  # http://127.0.0.1:8000/projects/?page=2
    except PageNotAnInteger:
        page = 1
        pr = paginator.page(page)  # http://127.0.0.1:8000/projects/?page=fgdfgdfg
    except EmptyPage:
        page = paginator.num_pages
        pr = paginator.page(page)  # http://127.0.0.1:8000/projects/?page=100

    left_index = int(page) - 4
    if left_index < 1:
        left_index = 1

    right_index = int(page) + 5
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, pr


def search_projects(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    pr = Project.objects.filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query)
    )

    return pr, search_query