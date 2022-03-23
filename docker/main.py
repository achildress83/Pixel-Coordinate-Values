from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from rectangle import Rectangle
import numpy as np

app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData):
    if not postedData:
        return 400
    # check whether dimensions are positive
    min_dim = min(postedData['image_dimensions'])

    # check whether any negative values for corner points
    neg_nums = np.sum(np.array([min(i) for i in postedData['corner_points']]) < 0)

    # get sets of x and y corner points (should be 2 unique numbers per set)
    x_unique = set([i[0] for i in postedData['corner_points']])
    y_unique = set([i[1] for i in postedData['corner_points']])

    # error 1: not a rectangle
    if len(x_unique) != 2 or len(y_unique) != 2:
        return 301
    # error 2: not in first quadrant
    elif neg_nums > 0:
        return 302
    # error 3: not a tensor
    elif min_dim < 0:
        return 303
    else:
        return 200

class Solution(Resource):

    def get(self):
        return {'hello': 'world'}

    def post(self):

        # get posted data
        postedData = request.get_json()
        """
            *** note ***
            Please make sure you set content-type to "application/json" in the request header.
            Otherwise your request body will be empty.

            example_post = {
                "image_dimensions": (10, 12),
                "corner_points": [
                    (1.5, 1.5),
                    (4.0, 1.5),
                    (1.5, 8.0),
                    (4.0, 8.0)
                ]
            }
        """
        # verify validity of posted data
        status_code = checkPostedData(postedData)
        if (status_code != 200):
            if status_code == 301:
                retJson = {
                    "Message": "not a rectangle",
                    "Status Code":  status_code
                }
            elif status_code == 302:
                retJson = {
                    "Message": "not in first quadrant",
                    "Status Code":  status_code
                }
            elif status_code == 303:
                retJson = {
                    "Message": "not a tensor",
                    "Status Code":  status_code
                }
            elif status_code == 400:
                retJson = {
                    "Message": "bad request",
                    "Status Code":  status_code
                }

                return jsonify(retJson)

        image_dimensions = postedData['image_dimensions']
        corner_points = postedData['corner_points']
        ret = Rectangle(image_dimensions, corner_points)

        retMap = {
            'Message': ret.create_matrix(),
            'Status Code': 200
        }

        return jsonify(retMap)

api.add_resource(Solution,'/')

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
