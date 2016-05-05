# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "{{ auth_token }}"
client = TwilioRestClient(account_sid, auth_token)

numbers = client.phone_numbers.search(area_code="800",
    country="US",
    contains="KYLO",
    type="tollfree")
# Purchase the first number in the list
if numbers:
    numbers[0].purchase()