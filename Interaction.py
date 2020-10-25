from twilio.rest import Client
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from WebScraper import WebScraper


class Intro:

    account_sid = 'ACb05b30eabad7258cc53c02ca565f882e'
    account_token = '065e7dc0674e1c6361e5e0199a89a9e8'

    def sendIntro(self):
        client = Client(Intro.account_sid, Intro.account_token)

        client.messages.create(
            to= '+15132837210',
            from_='+17032918270',
            body="Welcome to the covid-19 tracker! What state would you like to recieve info on?"

        )

class GetData:
    def getData(self, state):
        data = WebScraper().getInfo()
        info = data[str(state).upper()]

        return info

    def getInfo(self):
        data = WebScraper().getInfo()
        return data

start = Intro().sendIntro()

app = Flask( __name__ )


@app.route( "/sms", methods=['POST'] )
def sms_reply() :



    from_number = request.form['From']
    to_number = request.form['To']
    body = request.form['Body']

    keys = list(GetData().getInfo().keys())

    valid = False
    if str(body).upper() in keys:
        valid = True

    message = ''

    if valid:
        message = f"There are {GetData().getData(body)} cases of COVID-19 in {str(body).upper()}"

    else:
        message = "Invaid input try again"




    resp = MessagingResponse()


    resp.message( message )

    return str( resp )


if __name__ == "__main__" :
    app.run( debug=True )
