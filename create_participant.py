# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)
participant = client.proxy \
                    .services('ServiceSID') \
                    .sessions('SessionSID') \
                    .participants \
                    .create(identifier='whatsapp:+participant_1/2', proxy_identifier="whatsapp:+ProxyIdentifierTwilioNumber")

print(participant.proxy_identifier)