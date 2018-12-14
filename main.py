import config

import logging
from flask import jsonify, json
from helpers import DialogFlowService

def get_request_objects(request):

    return request

def service_webhook(request):
    post = {
        'post': request.get_json(silent=True)
    }
    intent_name = post['queryResult']['intent']['displayName']
    session_id = post['session']
    response_id = post['responseId']

    # response
    response = {
        # "fulfillmentText": "Hola {} desde el webhook".format(nombre),
        "followupEventInput": {
            "name": intent_name,
            "parameters": {}
        }
    }

    # Split intents
    if intent_name == 'initent-a':
        print('intent a')

    elif intent_name == 'intent-b':
        print('intent b')

    # prepare reesponse
    json_response = jsonify(response)

    return json_response
