import tkinter as tk
import paho.mqtt.publish as publish

# MQTT Broker Details
mqtt_broker = "rule28.i4t.swin.edu.au"
mqtt_port = 1883
mqtt_username = "103517299"  # Your student ID
mqtt_password = "103517299"  # Same as username

# Define a callback function for the "Publish" button
def publish_message():
    message = entry.get()
    topic = "public/user_interface"
    publish.single(topic, message, hostname=mqtt_broker, port=mqtt_port, auth={'username': mqtt_username, 'password': mqtt_password})

# Create the tkinter GUI
root = tk.Tk()
root.title("IoT User Interface")

label = tk.Label(root, text="Enter a message:")
label.pack()

entry = tk.Entry(root)
entry.pack()

publish_button = tk.Button(root, text="Publish", command=publish_message)
publish_button.pack()

root.mainloop()
