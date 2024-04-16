import paho.mqtt.client as mqtt

# MQTT broker settings
MQTT_BROKER_HOST = '120.101.8.113'
MQTT_BROKER_PORT = 1888

# INX-MQTT topics
TOPIC_CONFIRMED = '$IOTA/tangle/confirmed'
TOPIC_UNCONFIRMED = '$IOTA/tangle/unconfirmed'

def on_connect(client, userdata, flags, rc):
    print('Connected to INX-MQTT (result code: %s)' % rc)
    # subscribe to topics
    client.subscribe(TOPIC_CONFIRMED)
    client.subscribe(TOPIC_UNCONFIRMED)

def on_message(client, userdata, msg):
    print('Received message on topic %s: %s' % (msg.topic, msg.payload))

# create MQTT client
client = mqtt.Client()

# set callback functions
client.on_connect = on_connect
client.on_message = on_message

# connect to MQTT broker
client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, 60)

# start MQTT client loop
client.loop_forever()
