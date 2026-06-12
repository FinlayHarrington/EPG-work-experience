import time
import random
import json
import paho.mqtt.client as mqtt
import time

BROKER = "10.10.30.58"
TOPIC = "temp"
TopicList = ["temp", "humidity", "pressure", "light", "co2"]

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, 1883)
client.loop_start()


payload = json.dumps({
    "val": 45
})
if TOPIC == "temp":
    client.publish(TOPIC, payload)
    print(f"Published: {payload}")
while True:
    random_value = random.randint(40, 50)
    random_value_Topic = random.randint(0, 4)
    payload = json.dumps({
    "val": random_value
    })
    TOPIC = TopicList[random_value_Topic]
    if TOPIC == "temp":
        client.publish(TOPIC, payload)
        print(f"Published: {TOPIC} {payload}")
    time.sleep(1)
