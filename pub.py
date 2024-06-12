import sys
import paho.mqtt.client as mqtt
server = "test.mosquitto.org"
#test.mosquitto.org
#iotlab101.io7lab.com
#iotlab101.tosshub.co

client = mqtt.Client()
client.connect(server, 1883, 60)

if len(sys.argv) <= 1:
    print("Usage : "+sys.argv[0]+" message")
    exit()
else:
    client.publish("sunghopi", str(sys.argv[1]))
