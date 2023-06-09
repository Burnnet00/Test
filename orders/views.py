from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from orders.models import SalesOrder
from orders.serializers import OrderSerializer


def orders_page(reguest):
    return render(reguest, "index.html", {'orders' : SalesOrder.objects.all()})

class OrderView(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerializer

def orders_app(reguest):
    return render(reguest, "main_app.html")