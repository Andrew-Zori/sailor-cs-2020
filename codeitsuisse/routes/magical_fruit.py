import logging
import json
import numpy as np

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def evaluateFruitbasket():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input");

    result = (guess_result(data["maApple"], data["maWatermelon"],data["maBanana"]))

    # result = inputValue * inputValue
    logging.info("My result :{}".format(result))
    return jsonify(result)

def guess_result(ma, mb, mc):
    wa = 60
    wb = 60
    wc = 60
    return (ma * wa + mb * wb + mc * wc)