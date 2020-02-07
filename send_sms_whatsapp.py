# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body="Template message",
                              from_='whatsapp:+proxyTwilioNumber',
                              to='whatsapp:+participant_2'
                          )

print(message.sid)
