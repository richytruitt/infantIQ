import json
import machine
import network
import ssl
import time
import ubinascii
from simple import MQTTClient
import config
import tls
import random
import ntptime

led = machine.Pin("LED", machine.Pin.OUT)

SSID = config.SSID
WIFI_PASSWORD = config.WIFI_PASSWORD

MQTT_CLIENT_ID = "infantIQ_Hudson"
MQTT_CLIENT_KEY = "certs/infantiq_hudson-private.pem.key"
MQTT_CLIENT_CERT = "certs/infantiq_hudson-certificate.pem.crt"

MQTT_BROKER = config.IOT_CORE_ENDPOINT
MQTT_BROKER_CA = "certs/AmazonRootCA1.pem"


def read_pem(file):
    with open(file, "r") as input:
        text = input.read().strip()
        split_text = text.split("\n")
        base64_text = "".join(split_text[1:-1])
        return ubinascii.a2b_base64(base64_text)

def connect_internet():
    try:
        sta_if = network.WLAN(network.STA_IF)
        sta_if.active(True)
        sta_if.connect(SSID, WIFI_PASSWORD)

        for i in range(0, 10):
            if not sta_if.isconnected():
                time.sleep(1)
        print("Connected to Wi-Fi")
    except Exception as e:
        print('There was an issue connecting to WIFI')
        print(e)


def generate_new_reading():

    button_options = ["diaper_change", "feeding", "nap"]
    selected_value = random.choice(button_options)

    
    payload = {
        "deviceID": MQTT_CLIENT_ID, 
        "timestamp": time.time(),
        "action": selected_value
    }
    
    
    mqtt_client.publish('infantiq/actions', json.dumps(payload))
    
def flash_led(times, led):
    for i in range(times):
        led.on()
        time.sleep(.2)
        led.off()
        time.sleep(.2)
    

connect_internet()
ntptime.settime()

context = ssl.SSLContext(tls.PROTOCOL_TLS_CLIENT)
context.load_cert_chain(read_pem(MQTT_CLIENT_CERT), read_pem(MQTT_CLIENT_KEY))
context.load_verify_locations(cadata=read_pem(MQTT_BROKER_CA))
context.verify_mode = ssl.CERT_REQUIRED

mqtt_client = MQTTClient(
    MQTT_CLIENT_ID,
    MQTT_BROKER,
    keepalive=60,
    ssl=context
)

mqtt_client.connect()

while True:
    generate_new_reading()
    time.sleep(30)
    
