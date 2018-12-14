import config

import logging
from flask import jsonify, json
#from helpers import DialogFlowService

def get_request_objects(request):

    return request

def service_webhook(request):
    post = request.get_json(silent=True)

    #request
    intent_name = post['queryResult']['intent']['displayName']
    parameters = post['queryResult']['parameters']

    # response
    response = {
        # "fulfillmentText": "Hola {} desde el webhook".format(nombre),
        "followupEventInput": {
            "name": intent_name,
            "parameters": {
                "respuesta": "mi respuesta {}.".format(str(parameters))
            }
        }
    }

    # prepare reesponse
    json_response = jsonify(response)

    return json_response
