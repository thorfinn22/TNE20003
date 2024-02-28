import paho.mqtt.client as mqtt
import time
import random

# MQTT Broker Details
mqtt_broker = "rule28.i4t.swin.edu.au"
mqtt_port = 1883
mqtt_username = "103517299"  # Your student ID
mqtt_password = "103517299"  # Same as username

# Define a private topic and a public topic
private_topic = "103517299/private_topic"
public_topic = "public/device1"

# Create a MQTT client
client = mqtt.Client("Device1")
client.username_pw_set(mqtt_username, mqtt_password)

# Define a callback for when the client receives a message
def on_message(client, userdata, message):
    print(f"Received message on topic '{message.topic}': {message.payload.decode()}")

# Set the callback function
client.on_message = on_message

# Connect to the MQTT broker
client.connect(mqtt_broker, mqtt_port)

# Subscribe to the private topic and the public topic
client.subscribe(private_topic)
client.subscribe("public/#")  # Subscribe to all subtopics of 'public'

while True:
    # Generate fake data (e.g., temperature reading)
    temperature = random.randint(20, 30)

    # Publish the data to the private topic and the public topic
    client.publish(private_topic, f"Temperature: {temperature} °C")
    client.publish(public_topic, f"Temperature: {temperature} °C")

    # Sleep for a while before publishing the next data
    time.sleep(10)
    
# Disconnect from the MQTT broker
client.disconnect()
