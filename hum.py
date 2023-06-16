import Adafruit_DHT
import time
from datetime import datetime
import os

# Sensor type
sensor = Adafruit_DHT.DHT11

# GPIO pin number
pin = 4

# Output file name
filename = "output.txt"

# Maximum file size (10MB/approx. 12.4 days)
max_size = 10 * 1024 * 1024

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Get the current date and time
    now = datetime.now()

    # Format the date and time as a string
    timestamp = now.strftime("%Y/%m/%dT%H:%M:%S")

    # Open the output file in append mode
    with open(filename, "a") as file:
        if humidity is not None and temperature is not None:
            # Write the datetime, temperature, and humidity to the file
            file.write('{0} Temp={1:0.1f}*C  Humidity={2:0.1f}%\n'.format(timestamp, temperature, humidity))
        else:
            # Write the datetime and an error message to the file
            file.write('{0} Failed to get reading. Try again!\n'.format(timestamp))

    # Check the file size
    if os.path.getsize(filename) > max_size:
        with open(filename, "r") as file:
            lines = file.readlines()

        # Remove the first line
        lines = lines[1:]

        # Write the remaining lines back to the file
        with open(filename, "w") as file:
            file.writelines(lines)

    # Delay before the next reading (5 seconds in this example)
    time.sleep(5)

