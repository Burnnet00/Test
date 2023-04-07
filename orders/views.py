from django.shortcuts import render

from orders.models import SalesOrder


def orders_page(reguest):
    return render(reguest, "index.html", {'orders' : SalesOrder.objects.all()})
