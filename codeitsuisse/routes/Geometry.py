import logging
import json
import numpy as np

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/revisitgeometry', methods=['POST'])
def evaluateGeometry():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input");

    result = (result_func(data["shapeCoordinates"], data["lineCoordinates"]))

    # result = inputValue * inputValue
    logging.info("My result :{}".format(result))
    return jsonify(result)
# dic_list {"x": , "y",}

def result_func(shape_cords, line_cords): 
    result = []
    shape_cords.append(shape_cords[0])

    l_x1 = line_cords[0]["x"]
    l_x2 = line_cords[1]["x"]

    l_y1 = line_cords[0]["y"]
    l_y2 = line_cords[1]["y"]

    a1 = l_y2 - l_y1
    b1 = l_x1 - l_x2
    c1 = l_y1 * l_x2 - l_y2 * l_x1

    for i in range(len(shape_cords)-1):
        x1 = shape_cords[i]["x"]
        y1 = shape_cords[i]["y"]

        x2 = shape_cords[i+1]["x"]
        y2 = shape_cords[i+1]["y"]

        a2 = y2 - y1
        b2 = x1 - x2
        c2 = y1 * x2 - y2 * x1
        
        if a1*b2 != a2*b1:
            x_intersect = (c1*b2-c2*b1)/(a2*b1-a1*b2)
            y_intersect = (a2*c1-a1*c2)/(a1*b2-a2*b1)

            if int(x_intersect) != x_intersect:
                x_intersect = round(x_intersect,2)
            else:
                x_intersect = int(x_intersect)
            if int(y_intersect) != y_intersect:
                y_intersect = round(y_intersect,2)
            else:
                y_intersect = int(y_intersect)

            if x_intersect <= max(x1,x2) and x_intersect >= min(x1,x2)\
               and y_intersect <= max(y1,y2) and y_intersect >= min(y1,y2):
                
                result.append({"x" : x_intersect,\
                           "y" : y_intersect})
    return result