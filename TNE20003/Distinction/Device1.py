import paho.mqtt.client as mqtt
import time
import random

# MQTT Broker Details
mqtt_broker = "rule28.i4t.swin.edu.au"
mqtt_port = 1883
mqtt_username = "103517299"  # Your student ID
mqtt_password = "103517299"  # Same as username

# Define private topics and a public topic for Device 1
private_topic = "103517299/devices/device1/private"
public_topic = "public/devices"

# Create a MQTT client for Device 1
client = mqtt.Client("Device1")
client.username_pw_set(mqtt_username, mqtt_password)

# Connect to the MQTT broker
client.connect(mqtt_broker, mqtt_port)

while True:
    # Generate fake temperature data
    temperature = random.uniform(20.0, 30.0)
    message = f"Temperature: {temperature} °C"
    
    # Publish data to private and public topics
    client.publish(private_topic, message)
    client.publish(public_topic, message)

    # Sleep for a while before publishing the next data
    time.sleep(10)
