import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import tkinter as tk
import time
import random
import threading

# MQTT Broker Details
mqtt_broker = "rule28.i4t.swin.edu.au"
mqtt_port = 1883
mqtt_username = "103517299"  # Your student ID
mqtt_password = "103517299"  # Same as username

# Define private topics and public topic
private_topics = {
    "device1": "103517299/devices/device1/private",
    "device2": "103517299/devices/device2/private",
    "device3": "103517299/devices/device3/private"
}
public_topic = "public/devices"
user_interface_topic = "public/user_interface"

# Create MQTT clients for each device
devices = ["device1", "device2", "device3"]
device_clients = {}

for device in devices:
    client = mqtt.Client(device)
    client.username_pw_set(mqtt_username, mqtt_password)
    device_clients[device] = client

# Define a callback function for the MQTT client to handle message received on private topic
def on_message(client, userdata, message):
    print(f"Received message on private topic: {message.payload.decode()}")

# Set the callback function for all MQTT clients
for device, client in device_clients.items():
    client.on_message = on_message

# Connect to the MQTT broker and subscribe to private topics for all devices
for device, client in device_clients.items():
    client.connect(mqtt_broker, mqtt_port)
    client.subscribe(private_topics[device])

# Start the MQTT client loops to handle incoming messages
for client in device_clients.values():
    client.loop_start()

# Function to generate and publish data for each device
def generate_and_publish_data():
    while True:
        for device in devices:
            if device == "device1":
                data = f"Temperature: {random.uniform(20.0, 30.0)} °C"
            elif device == "device2":
                data = f"Humidity: {random.uniform(40.0, 60.0)}%"
            else:
                data = f"Pressure: {random.uniform(900.0, 1100.0)} hPa"

            device_clients[device].publish(private_topics[device], data)
            device_clients[device].publish(public_topic, data)
        
        # Sleep for a while before publishing the next data
        time.sleep(10)

# Create a thread for data generation and publishing
data_thread = threading.Thread(target=generate_and_publish_data)
data_thread.daemon = True
data_thread.start()

# Create the tkinter GUI
root = tk.Tk()
root.title("IoT User Interface")

label = tk.Label(root, text="Enter a message:")
label.pack()

entry = tk.Entry(root)
entry.pack()

# Define a callback function for the "Publish" button
def publish_message():
    message = entry.get()
    publish.single(user_interface_topic, message, hostname=mqtt_broker, port=mqtt_port, auth={'username': mqtt_username, 'password': mqtt_password})

publish_button = tk.Button(root, text="Publish", command=publish_message)
publish_button.pack()

# Run the GUI
root.mainloop()
