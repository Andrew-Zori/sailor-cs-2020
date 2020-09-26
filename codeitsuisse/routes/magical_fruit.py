import logging
import json
import numpy as np

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def evaluateFruitbasket():
    data = request.get_data()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input");

    result = (guess_result(data[0], data[1],data[2]))

    # result = inputValue * inputValue
    logging.info("My result :{}".format(result))
    return jsonify(result)

def guess_result(ma, mb, mc):
    wa = 60
    wb = 60
    wc = 60
    return (int(ma) * wa + int(mb) * wb + int(mc) * wc)