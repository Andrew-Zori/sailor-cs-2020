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

    name_list = []
    for key in data.keys():
        name_list.append(key)

    weight = {name_list[0]: 60,
    name_list[1]: 60,
    name_list[2]: 60}

    for key, value in data.items():
        ans += weight[key] * value
    return str(ans)