import logging
import json
import numpy as np

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/salad-spree', methods=['POST'])
def evaluateSalad_Spree():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input");

    result = (find_salad(data["number_of_salads"], data["salad_prices_street_map"]))

    # result = inputValue * inputValue
    logging.info("My result :{}".format(result))
    return jsonify(result)

def find_salad(n, street_map):
    n = int(n)
    np_sm = np.array(street_map)
    find_one = False
    cheapest = 1000
    for street in np_sm:
        start = 0
        end = n
        while(end <= len(street)):
            if np.where(np.isin(street[start: end],np.array(["X"])))[0].size != 0:
                no_salad_index = np.isin(street,np.array(["X"]))[-1]
                end += no_salad_index + 1
                start += no_salad_index + 1
            else:
                to_sum = street[start:end].astype(np.int32)
                if find_one:
                    if np.sum(to_sum)<cheapest:
                        cheapest = np.sum(to_sum)
                else:
                    cheapest = np.sum(to_sum)
                    find_one = True
                end += 1
                start += 1
    dic = {}
    
    if find_one:
        dic["result"] = int(cheapest)
        return dic
    else:
        dic["result"] = 0
        return dic



