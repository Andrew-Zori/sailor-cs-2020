import logging
import json
from math import factorial

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/social_distancing', methods=['POST'])
def evaluateSocialDisctance():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input");
    result = {}
    for _, sample in data.items():
        for i, (_, value) in enumerate(sample.items()):
            result[str(i)] = int(num_sd(value["seats"],value["people"],value["spaces"]))

    to_return = {"answer" : result}
    # result = inputValue * inputValue
    logging.info("My result :{}".format(result))
    return jsonify(to_return)

def num_sd(n, people, space):
        if n == people + space * (people-1):
                return 1
        if n == people + space * (people-1) + 1:
                return (people + 1)
        if n == people + space * (people-1) + 2:
                return ( factorial(1+people)/(2 * factorial(people - 1)) + \
                         people + 1)

        # C( (n - (people - 1) * space)
        x = n - (people - 1) * space - people
        sum_1 = int(factorial(x + people - 2) / (factorial(x) * factorial(people - 2)))
        sum_2 = int(2 * factorial(x + people - 2) / (factorial(x-1) * factorial(people - 1)))
        sum_3 = int(factorial(x + people - 2) / (factorial(x-2) * factorial(people)))
        
        return (int(sum_1 + sum_2 + sum_3))



