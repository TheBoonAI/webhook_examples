import os
import pprint
import requests
import jwt


def slack_it(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    # Validate the Boon AI JWT
    jwt_valid = True
    encoded_jwt = request.headers.get('X-BoonAI-Signature-256').encode('utf-8')
    try:
        jwt.decode(encoded_jwt, os.environ['SECRET'], algorithms=["HS256"])
    except jwt.InvalidSignatureError:
        jwt_valid = False

    # Send a slack message with the payload information.
    body = {
        "text": "Webhook received from Boon AI",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": "Webhook received from Boon AI",
                    "emoji": True
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*JWT Validated*: {jwt_valid}\n "
                            f"*JWT*: {request.headers.get('X-BoonAI-Signature-256')}\n "
                            f"*Content-Type*: {request.content_type}\n "
                            f"*Webhook Payload*\n```{pprint.pformat(request.get_json(force=True))}```"
                }
            }
        ]
    }
    requests.post(os.environ['SLACK_URL'], json=body)

    return {}
