from django.shortcuts import render
from .models import Work


# Create your views here.
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
    return render(request, "work/detail.html", context)
