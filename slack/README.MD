# Slack Integration

The code here is designed to be deployed as a [Google Cloud Function](https://cloud.google.com/functions) 
however this code could easily be used in a [Flask](https://flask.palletsprojects.com) application or the equivalent cloud 
function services on other cloud providers.

## Install Instructions

1. Create an incoming webhook in Slack using this [guide](https://api.slack.com/messaging/webhooks#getting_started).
1. Create a new GCP cloud function using the [python quickstart guide](https://cloud.google.com/functions/docs/quickstart-python).
1. After the function is deployed choose it from the list of functions and click "Edit".
1. Add the following "Runtime Environment Variables":
    - SECRET: This is the secret token used for validating messages are actually from Boon AI. You can retrieve this from 
    the webhook you configured in Boon AI.
    - SLACK_URL - URL for the incoming webhook you configured in Slack earlier.
1. Use the inline editor in the GCP console to copy the contents of the requirements.txt and main.py from this repo to your cloud function.
1. Set the "Entry point" in the inline editor to "slack_it".
1. Deploy the webhook and note the url for triggering it.
1. Go to your Boon AI project in the developer console and create a webhook using the secret token you set and the URL for your
cloud function.
