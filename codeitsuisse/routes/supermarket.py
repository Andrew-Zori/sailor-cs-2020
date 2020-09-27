# Why no full score??

import logging
import json
import numpy as np

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/supermarket', methods=['POST'])
def evaluateSupermarket():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input");
    answer = {}

    for _, value_q in data.items():
        for key, value in (value_q.items()):
            answer[key] = step_count(value["maze"], value['start'], value['end'])

    # result = inputValue * inputValue
    result = {"answers" : answer}
    logging.info("My result :{}".format(result))
    return jsonify(result)

def step_count(A, start, end):
    A = np.array(A)
    inf_A = np.zeros(A.shape)
    dist_A = np.zeros(A.shape)
    dist_A[start[1]][start[0]] = 1

    find = False

    start = (start[1], start[0])
    
    Q = []
    Q.append(start)
    while (len(Q) != 0):
        u = Q.pop()
        adj_points = adjacent_points(u, A.shape[0], A.shape[1])
        for v in adj_points:
            if inf_A[v[0]][v[1]] == 0 and A[v[0]][v[1]] == 0:
                inf_A[v[0]][v[1]] = 0.5
                dist_A[v[0]][v[1]] = dist_A[u[0]][u[1]] + 1
                Q.append(v)
            if v == (end[1],end[0]):
                find = True
                Q = []
                break
        inf_A[u[0]][u[1]] = 1
        print(inf_A)

    if find:
        steps = dist_A[end[1]][end[0]]
    else:
        steps = -1

    return steps
                    


def adjacent_points(origin, length, breadth):
    # origin -> (row, col)
    adj_pts = []
    row = origin[0]
    col = origin[1]
    for i in range(row-1, row+2, 2):
        if i < 0 or i >= length:
            continue
        adj_pts.append((i, col))
        
    for j in range(col-1, col+2, 2):
        if j < 0 or j >= breadth:
            continue
        adj_pts.append((row,j))
    return adj_pts



