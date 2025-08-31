import random
from datetime import datetime
from sensor.models import SensorData

def generate_data():
    """
    Generate random sensor data.
    """
    return {
        "timestamp": datetime.now(),
        "temperature": round(random.uniform(20, 30), 2),
        "humidity": round(random.uniform(30, 70), 2),
        "energy": round(random.uniform(0, 500), 2)
    }

def save_data():
    """
    Save generated sensor data to the database.
    """
    data = generate_data()
    SensorData.objects.create(
        timestamp=data["timestamp"],
        temperature=data["temperature"],
        humidity=data["humidity"],
        energy=data["energy"]
    )

def run():
    for _ in range(10):
        save_data()