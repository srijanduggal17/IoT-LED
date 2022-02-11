from flask import Flask, request, jsonify
from gpiozero import LED

app = Flask(__name__, instance_relative_config=True)

led = LED(26)
led.off()

@app.route('/oven', methods=['POST'])
def hello():
    oven_on = request.json['oven']
    if oven_on:
        led.on()
        return 'Oven is on'
    else:
        led.off()
        return 'Oven is off'

app.run(host='0.0.0.0', port=5000)
