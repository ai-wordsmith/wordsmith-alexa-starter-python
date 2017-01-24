"""
This file is intended to be a very simple version of the lambda_function.py
blueprint. This file provides the framework to provide a single response to an
Alexa skill with no card data, reprompt text, etc included.

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function
import wordsmith_basic as wordsmith

WORDSMITH_API_KEY = '<YOUR API KEY HERE>'
WORDSMITH_PROJECT_SLUG = '<YOUR PROJECT SLUG HERE>'
WORDSMITH_TEMPLATE_SLUG = '<YOUR TEMPLATE SLUG HERE>'

# --------------- Helpers that build all of the responses ----------------------


def build_response(output, should_end_session):
    return {
        'version': '1.0',
        'sessionAttributes': {},
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': output
            },
            'shouldEndSession': should_end_session
        }
    }


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    intent = event['request']['intent']
    intent_name = event['request']['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "<YOUR INTENT NAME HERE>":
        # Update the wordsmith_data variable with your data. Use key, value
        # pairs where the key is the column name in Wordsmith and the value is
        # the value contained in that column
        wordsmith_data = { 'column1': 'value1', 'column2': 'value2' }
        narrative = wordsmith.generate(WORDSMITH_API_KEY, WORDSMITH_PROJECT_SLUG, WORDSMITH_TEMPLATE_SLUG, wordsmith_data)
        if 'errors' not in narrative:
            return build_response(narrative['data']['content'], True)
        else:
            if not isinstance(narrative['errors'], list):
                return build_response('Wordsmith reported the following error {}'.format(narrative['errors']['detail']), True)
            else:
                details = ', '.join([e['details'] for e in narrative['errors']])
                return build_response('Wordsmith reported the following errors {}'.format(details), True)
    else:
        raise ValueError("Invalid intent")

