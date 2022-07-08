from .models import Course, Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q


def searchCourses(request):
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')

    tags = Tag.objects.filter(name__icontains=search)
    courses = Course.objects.distinct().filter(
        Q(title__icontains=search) | Q(owner__name__icontains=search) | Q(tags__in=tags))
    return courses, search


def paginationCourses(request, courses, results):
    page = request.GET.get('page')

    paginator = Paginator(courses, results)

    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        courses = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        courses = paginator.page(page)

    left_index = (int(page)-4)

    if left_index < 1:
        left_index = 1

    right_index = (int(page)+5)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, courses
