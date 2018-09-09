import testingIntent
import testingIntent

db_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJyb2xlIjoicGF0aWVudCIsImlhdCI6MTUzNjQzNjQxOSwiZXhwIjoxNTk5NTA4NDE5fQ.z7eRo6TiGrhEW5dK2_-V6d2MK8hT40RZ-ztecYjIjPQ"

def lambda_handler(event, context):
    request = event
    print event
    response = None
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
    if request["request"]["type"] == "IntentRequest":
        if request["request"]["intent"]["name"] == "testing":
            response = testingIntent.testingIntentHandler(event, context)
        elif request["request"]["intent"]["name"] == "pendingMedication":
            response = pendingMedicationIntent.pendingMedicationIntentHandler(event, context, db_token)
        elif request["request"]["intent"]["name"] == "takenMedicine":
            response =
    return response
if __name__ == "__main__":
    lambda_handler("test", "hi")