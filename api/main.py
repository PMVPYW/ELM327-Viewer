import elm327

import time

elm = elm327.ELM327Reader('/dev/' + input("Enter the name of the ELM327 device: "))
elm.start_listening()
print("Listening to OBD data... Press Ctrl+C to stop.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping OBD data listening...")
    elm.stop_listening()
    print("Data collection stopped.")
    data = elm.get_data()
    print("Collected Data:")
    for key, values in data.items():
        print(f"{key}: {values}")