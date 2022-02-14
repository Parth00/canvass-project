import time
import random
import xmlrpc.client as client
from datetime import datetime as dt

TIME_FORMAT = "%Y-%m-%dT%H:%M:%S"

class SensorDevice:
    """
    Class to manage Sensor Devices
    """
    def __init__(self, id, pressure, status, temperature):
        self.id = id
        self.pressure = pressure
        self.status = status
        self.temperature = temperature
        self.timestamp = dt.now().strftime(TIME_FORMAT)

    def json_format(self):
        """
        Returns data in JSON format
        """
        return {
            "deviceId": self.id,
            "timestamp": self.timestamp,
            "pressure": f'{self.pressure:.2f}',
            "status": self.status,
            "temperature": f'{self.temperature:.2f}'
        }


if __name__ == '__main__':
    server_proxy = client.ServerProxy('http://localhost:8000/')

    _status = ["ON", "OFF", "ACTIVE", "INACTIVE"]

    
    for _ in range(5):
        id = random.randint(1, 10)
        pressure = random.uniform(100.00, 1000.00)
        status = random.choice(_status)
        temperature = random.uniform(25.00, 250.00)

        device = SensorDevice(f"sensor-{id}", pressure, status, temperature)
        server_proxy.store(device.json_format())

        time.sleep(3)
    
    server_proxy.histogram(f'sensor-{random.randint(1,10)}')
