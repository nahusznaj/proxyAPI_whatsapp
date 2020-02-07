# proxyAPI_whatsapp

Instructions to use Twilio's Proxy API with Whatsapp numbers are proxy (masked).

Create a Service 

Create a Session - message only (!)

Twilio number does not need to be added in the Service 

Twilio number for whatsapp's webhook needs to be passed manually: `https://webhooks.twilio.com/v1/Accounts/{AccountSID}/Proxy/{ServiceSID}/Webhooks/Message`

Create participant_1 specifying the ProxyIdentifier

Create the second participant_2, specifying the ProxyIdentifier

Send a template message from Twilio Whatsapp number from rest API to participant_2. 

When participant_2 responds to Twilio Whatsapp number, participant_1 will receive a message from Twilio Whatsapp number. After this, both participants can message each other.
