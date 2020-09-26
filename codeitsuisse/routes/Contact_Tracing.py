import logging
import json
import numpy as np

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/contact_trace', methods=['POST'])
def evaluateContactTrace():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input");

    result = []
    for test_case in data:
        result.append(encrypt(test_case["n"], test_case["text"]))

    # result = inputValue * inputValue
    logging.info("My result :{}".format(result))
    return jsonify(result)



