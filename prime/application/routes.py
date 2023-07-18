from flask import Flask, jsonify, Response 
from flask import jsonify
import sys
from flask import jsonify
import json
from flask import json

app = Flask(__name__)

@app.route('/date/<ageInMonths>', methods=['GET', 'POST'])
def prime(ageInMonths):
    try:
        ageMonths = int(float(ageInMonths))
    except ValueError:
        return "ValueError: please enter a number"
    if ageMonths < 1:
        return 'You do not appear to exist'
    elif ageMonths == 1:
        return 'neither prime nor composite'
    elif ageMonths > 1:
        for i in range(2, ageMonths):
            if ageMonths % i == 0: #if age in months in divisible by i then composite, exit statement if it is not divisible
                return 'composite'
        return 'prime' 
    