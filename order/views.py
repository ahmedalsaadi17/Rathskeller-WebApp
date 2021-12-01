from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.http import JsonResponse
from .models import OrderItem

# Create your views here.


def order_list(request):
    ordered_items = OrderItem.objects.all()
    return render(request, "order/order_items.html", {"ordered_items": ordered_items})


def add_item(request):
    if request.method == "POST":
        if request.htmx:
            total = request.POST.get("total")
            print(total)
            try:
                session = Session.objects.get(session_key=request.session.session_key)
            except Exception:   
                request.session.create()
        return JsonResponse({"ok": "Item Added"})
    else:
        print("get request")
        return render(request, "rath/partials/success.html")
