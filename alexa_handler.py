import json

import requests


def lambda_handler(event, context):
    request = json.loads(event)
    apiToken = request["context"]["apiAccessToken"]
    apiEndpoint = request["context"]["apiEndpoint"]
    requestid = request["request"]["requestId"]
    name = request["request"]["intent"]["slots"]["name"]["value"]
    requests.post(apiEndpoint + "/v1/directives",
                  data={"Authorization": "Bearer " + apiToken, "Content-Type": "application/json"},
                  json={
                      "header": {
                          "requestId": requestid
                      },
                      "directive": {
                          "type": "VoicePlayer.Speak",
                          "speech": {
                              "type": "SSML",
                              "ssml": "<speak>The Name you gave to me <emphasis level='strong'>Rachit</emphasis> is <say-as interpret-as='characters'>{}</say-as></speak>".format(
                                  name)
                          }
                      }
                  })

    return {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "Rachit, your test worked successfully!",
            },
        },
        "shouldEndSession": True
    }


if __name__ == "__main__":
    lambda_handler("test", "hi")
