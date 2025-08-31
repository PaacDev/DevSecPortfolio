from django.test import TestCase
from django.urls import reverse
from .models import SensorData
from datetime import datetime, timedelta

class DashboardViewTest(TestCase):

    def setUp(self):
        # Creamos datos de prueba
        now = datetime.now()
        SensorData.objects.create(temperature=20.5, humidity=50.0, energy=100.0, timestamp=now)
        SensorData.objects.create(temperature=22.0, humidity=55.0, energy=110.0, timestamp=now + timedelta(minutes=10))

    def test_dashboard_status_code(self):
        """La view responde con código 200"""
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_template(self):
        """Se utiliza el template correcto"""
        response = self.client.get(reverse("dashboard"))
        self.assertTemplateUsed(response, "sensor/dashboard.html")

    def test_dashboard_context_data(self):
        """El contexto contiene listas de datos correctas"""
        response = self.client.get(reverse("dashboard"))
        data = SensorData.objects.all().order_by("timestamp")
        
        expected_labels = [d.timestamp.strftime("%Y-%m-%d %H:%M") for d in data]
        expected_temperatures = [d.temperature for d in data]
        expected_humidity = [d.humidity for d in data]
        expected_energy = [d.energy for d in data]

        self.assertEqual(response.context["labels"], expected_labels)
        self.assertEqual(response.context["temperatures"], expected_temperatures)
        self.assertEqual(response.context["humidity"], expected_humidity)
        self.assertEqual(response.context["energy"], expected_energy)
