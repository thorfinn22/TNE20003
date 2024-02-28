import paho.mqtt.client as mqtt
import time
import random

# MQTT Broker Details
mqtt_broker = "rule28.i4t.swin.edu.au"
mqtt_port = 1883
mqtt_username = "103517299"  # Your student ID
mqtt_password = "103517299"  # Same as username

# Define a private topic
private_topic = "103517299/private_topic"

# Create a MQTT client
client = mqtt.Client("Device1")
client.username_pw_set(mqtt_username, mqtt_password)

# Connect to the MQTT broker
client.connect(mqtt_broker, mqtt_port)

while True:
    # Generate fake data (e.g., temperature reading)
    temperature = random.randint(20, 30)

    # Publish the data to the private topic
    client.publish(private_topic, f"Temperature: {temperature} °C")

    # Sleep for a while before publishing the next data
    time.sleep(10)
    
# Disconnect from the MQTT broker
client.disconnect()
