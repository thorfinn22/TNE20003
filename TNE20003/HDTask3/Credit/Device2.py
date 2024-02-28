import paho.mqtt.client as mqtt

# MQTT Broker Details
mqtt_broker = "rule28.i4t.swin.edu.au"
mqtt_port = 1883
mqtt_username = "103517299"  # Your student ID
mqtt_password = "103517299"  # Same as username

# Define a private topic to subscribe to
private_topic = "103517299/private_topic"

# Create a MQTT client
client = mqtt.Client("Device2")
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

# Start the MQTT client loop to listen for messages
client.loop_forever()
