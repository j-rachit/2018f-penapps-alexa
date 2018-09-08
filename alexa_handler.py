db_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJyb2xlIjoicGF0aWVudCIsImlhdCI6MTUzNjQzNjQxOSwiZXhwIjoxNTk5NTA4NDE5fQ.z7eRo6TiGrhEW5dK2_-V6d2MK8hT40RZ-ztecYjIjPQ"

def lambda_handler(event, context):
    request = event
    print event
    if request["request"]["type"] == "LaunchRequest":
        return {
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "SSML",
                    "ssml": "<speak>Hi!<audio src='https://s3.amazonaws.com/ask-soundlibrary/musical/amzn_sfx_bell_short_chime_03.mp3'/>\
                    I can tell you if you've taken your medicine,\
                     information about your medication, or I can remind you to take your medication. What would you like to do?</speak>",
                },
                "shouldEndSession": False
            }
        }
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


if __name__ == "__main__":
    lambda_handler("test", "hi")