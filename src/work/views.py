from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Work
from .forms import WorkForm, RawWorkForm


# Create your views here.

def work_list_view(request):
    query_set = Work.objects.all() # list of objects
    context = {
        "object_list": query_set

    }
    return render(request, "work/work_list.html", context)


def work_delete_view(request, id):
    obj = get_object_or_404(Work, id=id)
    # GET request
    # obj.delete()
    if request.method == "POST":
        # confirming delete
        obj.delete()
        return redirect("../../")
    context = {
        "object": obj
    }
    return render(request, "work/work_delete.html", context)


def dynamic_lookup_view(request, id):
    # try:
    #     obj = Work.objects.get(id=id)
    # except Work.DoesNotExist:
    #     raise Http404
    obj = get_object_or_404(Work, id=id)
    context = {
        "object": obj
    }
    return render(request, "work/work_detail.html", context)


def render_initial_data(request):
    initial_data = {
        "project": "This is my selected project",
    }
    obj = Work.objects.get(id=1)
    form = WorkForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "work/work_create.html", context)


# def work_create_view(request):
#     my_form = RawWorkForm()
#     if request.method == "POST":
#         my_form = RawWorkForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Work.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "work/work_create.html", context)


# def work_create_view(request):
#     # print(request.GET)
#     # print(request.POST)
#     if request.method == "POST":
#         my_new_project = request.POST.get('project')
#         print(my_new_project)
#         # Work.objects.create(project=my_new_project)
#
#     context = {}
#     return render(request, "work/work_create.html", context)


def work_create_view(request):
    form = WorkForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = WorkForm()

    context = {
        'form': form
    }
    return render(request, "work/work_create.html", context)


def work_detail_view(request):
    obj = Work.objects.get(id=1)
    # context = {
    #     'project': obj.project,
    #     'hours': obj.hours,
    #     'work_descriptions': obj.work_descriptions,
    #     'date': obj.date,
    # }
    context = {
        'object': obj
    }
    return render(request, "work/work_detail.html", context)
