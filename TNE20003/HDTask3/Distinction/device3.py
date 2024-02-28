import paho.mqtt.client as mqtt
import time
import random

# MQTT Broker Details
mqtt_broker = "rule28.i4t.swin.edu.au"
mqtt_port = 1883
mqtt_username = "103517299"  # Your student ID
mqtt_password = "103517299"  # Same as username

# Define private topics and a public topic for Device 3
private_topic = "103517299/devices/device3/private"
public_topic = "public/devices"

# Create a MQTT client for Device 3
client = mqtt.Client("Device3")
client.username_pw_set(mqtt_username, mqtt_password)

# Connect to the MQTT broker
client.connect(mqtt_broker, mqtt_port)

while True:
    # Generate fake pressure data
    pressure = random.uniform(900.0, 1100.0)
    message = f"Pressure: {pressure} hPa"
    
    # Publish data to private and public topics
    client.publish(private_topic, message)
    client.publish(public_topic, message)

    # Sleep for a while before publishing the next data
    time.sleep(10)
