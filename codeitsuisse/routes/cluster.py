import logging
import json
import numpy as np

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/cluster', methods=['POST'])
def evaluateCluster():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input");
    result = {"answer": cluster(data)}

    # result = inputValue * inputValue
    logging.info("My result :{}".format(result))
    return jsonify(result)

def cluster(A):
    A = np.array(A)
    inf_A = np.zeros(A.shape)

    inf_ind_l = []

    for row in range(len(A)):
        for col in range(len(A[0])):
            if A[row][col] == "1":
                inf_ind_l.append((row,col))
                # inf_A[row][col] = 1

    cluster_num = 0

    for origin in inf_ind_l:
        if inf_A[origin[0]][origin[1]] == 0:
            cluster_num += 1
            # inf_A[origin[0]][rogin[1]] = 1
            Q = []
            Q.append(origin)
            while (len(Q) != 0):
                u = Q.pop()
                adj_points = adjacent_points(u, A.shape[0], A.shape[1])
                for v in adj_points:
                    if inf_A[v[0]][v[1]] == 0 and A[v[0]][v[1]] != "*":
                        inf_A[v[0]][v[1]] = 0.5
                        Q.append(v)
                inf_A[u[0]][u[1]] = 1
    return cluster_num
                    


def adjacent_points(origin, length, breadth):
    # origin -> (row, col)
    adj_pts = []
    row = origin[0]
    col = origin[1]
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i < 0 or i >= length or \
               j < 0 or j >= breadth:
                continue
            adj_pts.append((i,j))
    return adj_pts



