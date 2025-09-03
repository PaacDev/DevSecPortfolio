from django.shortcuts import render
from .models import SensorData
from django.views.decorators.http import require_GET


@require_GET
def dashboard(request):
    data = SensorData.objects.all().order_by("timestamp")

    context = {
        "labels": [d.timestamp.strftime("%Y-%m-%d %H:%M") for d in data],
        "temperatures": [d.temperature for d in data],
        "humidity": [d.humidity for d in data],
        "energy": [d.energy for d in data],
    }

    return render(request, "sensor/dashboard.html", context)
