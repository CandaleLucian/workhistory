from django.urls import path
from work.views import (work_detail_view,
                        work_create_view,
                        work_update_view,
                        work_delete_view,
                        work_list_view,
                        )
app_name = "work"
urlpatterns = [
    path('', work_list_view, name='work_list'),
    path('create/', work_create_view, name='work_create'),
    path('<int:id>/', work_detail_view, name="work_detail"),
    path('<int:id>/update/', work_update_view, name="work_update"),
    path('<int:id>/delete/', work_delete_view, name="work_delete"),
]
