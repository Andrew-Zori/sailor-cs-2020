import logging
import json
import numpy as np

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/clean_floor', methods=['POST'])
def evaluateClean_floor():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input");
    answer = {}

    for _, value_q in data.items():
        for key, value in (value_q.items()):
            answer[key] = clean_per_floor(value["floor"])

    # result = inputValue * inputValue
    result = {"answers" : answer}
    logging.info("My result :{}".format(result))
    return jsonify(result)

def clean_per_floor(floor):
    answers = 0
    position = 0
    floor.append(0)

    while sum(floor) != 0:
        if (position == 0 or sum(floor[position+1:])!=0):
            # move right
            position += 1
            answers += 1
            if (floor[position] == 0):
                floor[position] += 1
            else:
                floor[position] -= 1

        else:
            #move left
            position -= 1
            answers += 1
            if (floor[position] == 0):
                floor[position] += 1
            else:
                floor[position] -= 1
    return answers



