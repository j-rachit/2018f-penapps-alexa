import ast
import json
import time

import requests


def pendingMedicationIntentHandler(event, context, token):
    # http://pennapps.us-east-1.elasticbeanstalk.com/api/medication?token=
    medications = \
    json.loads(requests.get("http://pennapps.us-east-1.elasticbeanstalk.com/api/medication?token=" + token).text)[
        "medications"]
    for thing in medications:
        if ast.literal_eval(thing["days"])[int(time.strftime("%w"))] == 0:
            del thing
            continue
        thing["startTimeH"] = int(thing["startTimeH"])
        thing["startTimeM"] = int(thing["startTimeM"])
        thing["endTimeH"] = int(thing["endTimeH"])
        thing["endTimeM"] = int(thing["endTimeM"])
    textresponse = "<speak><prosody pitch='high'>Okay!</prosody>\
    Today you have to take {} pills. <break strength='strong'/>".format(len(medications))

    for loop in range(len(medications)):
        if medications[loop]["startTimeH"] <= 10:
            timeofday = "morning"
        elif 14 >= medications[loop]["startTimeH"] > 10:
            timeofday = "afternoon"
        elif 19 >= medications[loop]["startTimeH"] > 14:
            timeofday = "evening"
        else:
            timeofday = "night"
        textresponse += "<p><emphasis level='strong'><say-as interpret-as='number'>{}</say-as></emphasis>, In the {} <s>you need to \
        take {} between\
         {} {} and {} {}.</s><s>{} that is {}, you need to {}.</s></p><break time='1s'/> \n".format(
            str(loop + 1), timeofday, medications[loop]["brandName"], str(medications[loop]["startTimeH"]),
            str(medications[loop]["startTimeM"]),
            str(medications[loop]["endTimeH"]), str(medications[loop]["endTimeM"]), medications[loop]["brandName"],
            medications[loop]["description"], medications[loop]["instructions"])
    textresponse += "</speak>"
    return {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "SSML",
                "ssml": textresponse,
            },
        },
        "shouldEndSession": True
    }
