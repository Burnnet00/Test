from django.shortcuts import render

def orders_page(reguest):
    return render(reguest, "index.html")

