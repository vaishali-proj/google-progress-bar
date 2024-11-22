from machine import UART, Pin
import time
from esp8266 import ESP8266

# Initialize ESP8266
esp01 = ESP8266()
led = Pin(25, Pin.OUT)

print("StartUP:", esp01.startUP())
print("Echo-Off:", esp01.echoING())

print("\r\nESP8266 AT Version:")
esp8266_at_var = esp01.getVersion()
if esp8266_at_var:
    print(esp8266_at_var)

# Set WiFi mode
esp01.setCurrentWiFiMode()

# Connect to WiFi
print("Connecting to WiFi...")
while True:
    if "WIFI CONNECTED" in esp01.connectWiFi("Shreeja iphone", "shreeja123"):
        print("ESP8266 connected to WiFi.")
        break
    else:
        print("Retrying...")
        time.sleep(2)

print("\r\nHTTP Operations Begin...\r\n")
while True:
    led.toggle()
    time.sleep(1)

    # HTTP GET Example
    http_code, http_res = esp01.doHttpGet("www.httpbin.org", "/ip", "RaspberryPi-Pico", port=80)
    print("HTTP GET Result:")
    print("HTTP Code:", http_code)
    print("HTTP Response:", http_res)
    print("\r\n")

    # HTTP POST Example
    http_code, http_res = esp01.doHttpPost(
        "www.httpbin.org", "/post", "application/json", '{"key": "value"}', "RaspberryPi-Pico", port=80
    )
    print("HTTP POST Result:")
    print("HTTP Code:", http_code)
    print("HTTP Response:", http_res)
    print("\r\n")

