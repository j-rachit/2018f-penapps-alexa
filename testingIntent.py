def testingIntentHandler(request, context):
    if "value" not in request["request"]["intent"]["slots"]["name"]:
        return {
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "SSML",
                    "ssml": "<speak>What name do you want to test?</speak>",
                },
                "shouldEndSession": False,
                "directives": [
                    {
                        "type": "Dialog.ElicitSlot",
                        "slotToElicit": "name",
                    }
                ],
            }
        }
    name = request["request"]["intent"]["slots"]["name"]["value"]
    return {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "SSML",
                "ssml": "<speak>The Name you gave to me <emphasis level='strong'>Rachit</emphasis> is <say-as interpret-as='characters'>{}</say-as></speak>".format(
                    name),
            },
        },
        "shouldEndSession": True
    }
