from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .models import SaleOrder
from .forms import SaleOrderModelForm


# Create your views here.
class SaleOrderCreateView(CreateView):  # <app_name/<modelname>_list.html
    template_name = "sale_order/sale_order_create.html"
    form_class = SaleOrderModelForm
    queryset = SaleOrder.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class SaleOrderListView(ListView):
    template_name = "sale_order/sale_order_list.html"
    queryset = SaleOrder.objects.all()


class SaleOrderDetailView(DetailView):
    template_name = "sale_order/sale_order_detail.html"

    # queryset = SaleOrder.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(SaleOrder, id=id_)


class SaleOrderUpdateView(UpdateView):
    template_name = "sale_order/sale_order_create.html"
    form_class = SaleOrderModelForm
    queryset = SaleOrder.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(SaleOrder, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class SaleOrderDeleteView(DeleteView):
    template_name = "sale_order/sale_order_delete.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(SaleOrder, id=id_)

    def get_success_url(self):
        return reverse("sale_order:order_list")

