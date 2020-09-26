import logging
import json
import numpy as np

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def evaluatefruit():
    data = request.get_data()
    data = json.loads(data.decode('utf-8'))
    ans = 0

    weight = {"maApple": 60,
    "maWatermelon": 60,
    "maBanana": 60}

    for key, value in data.items():
        ans += weight[key] * value
    return str(ans)

def guess_result(ma, mb, mc):
    wa = 60
    wb = 60
    wc = 60
    return (int(ma) * wa + int(mb) * wb + int(mc) * wc)
    # return (mb)