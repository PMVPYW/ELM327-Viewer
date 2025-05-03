import obd
from pint import Quantity
import time

class ELM327Reader:
    def __init__(self, path: str):
        self.__path = path
        self.__connection = obd.Async(self.__path)
        self.__storage = {
            "FUEL_STATUS": [],
            "ENGINE_LOAD": [],
            "COOLANT_TEMP": [],
            "INTAKE_PRESSURE": [],
            "RPM": [],
            "SPEED": [],
            "THROTTLE_POS": []
        }
        self.begin = 0  # Timestamp when listening starts

    # Watchers for each OBD parameter
    def fuel_status_watcher(self, value: Quantity):
        self.__storage["FUEL_STATUS"].append({'value': value.value.magnitude if value.value is not None else None, 'time': time.time() - self.begin})

    def engine_load_watcher(self, value: Quantity):
        self.__storage["ENGINE_LOAD"].append({'value': value.value.magnitude if value.value is not None else None, 'time': time.time() - self.begin})

    def coolant_temp_watcher(self, value: Quantity):
        self.__storage["COOLANT_TEMP"].append({'value': value.value.magnitude if value.value is not None else None, 'time': time.time() - self.begin})

    def intake_pressure_watcher(self, value: Quantity):
        self.__storage["INTAKE_PRESSURE"].append({'value': value.value.magnitude if value.value is not None else None, 'time': time.time() - self.begin})

    def rpm_watcher(self, value: Quantity):
        self.__storage["RPM"].append({'value': value.value.magnitude if value.value is not None else None, 'time': time.time() - self.begin})

    def speed_watcher(self, value: Quantity):
        self.__storage["SPEED"].append({'value': value.value.magnitude if value.value is not None else None, 'time': time.time() - self.begin})

    def throttle_pos_watcher(self, value: Quantity):
        self.__storage["THROTTLE_POS"].append({'value': value.value.magnitude if value.value is not None else None, 'time': time.time() - self.begin})

    # Start listening to the OBD connection
    def start_listening(self):
        self.__connection.watch(obd.commands.FUEL_STATUS, callback=self.fuel_status_watcher)
        self.__connection.watch(obd.commands.ENGINE_LOAD, callback=self.engine_load_watcher)
        self.__connection.watch(obd.commands.COOLANT_TEMP, callback=self.coolant_temp_watcher)
        self.__connection.watch(obd.commands.INTAKE_PRESSURE, callback=self.intake_pressure_watcher)
        self.__connection.watch(obd.commands.RPM, callback=self.rpm_watcher)
        self.__connection.watch(obd.commands.SPEED, callback=self.speed_watcher)
        self.__connection.watch(obd.commands.THROTTLE_POS, callback=self.throttle_pos_watcher)
        self.begin = time.time()
        self.__connection.start()

    # Stop listening to the OBD connection
    def stop_listening(self):
        self.__connection.stop()
        self.__connection.unwatch_all()

    # Retrieve the stored data
    def get_data(self):
        return self.__storage
