import requests
import time
from gpiozero import LED

URL = 'https://fne3fcq235.execute-api.us-east-1.amazonaws.com/default/getOvenStatus'

led = LED(26)
led.off()

for i in range(1):
    r = requests.get(url = URL)
    data = r.json()
    print(data)
    if data[0]['oven_control'] == 1:
        led.on()
    elif data[0]['oven_control'] == 0:
        led.off()
    else:
        print('error')
    time.sleep(2)