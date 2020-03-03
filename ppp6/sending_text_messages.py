# SENDING TEXT MESSAGES
# twillio api

# 
from twillio.rest import Client
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

call = client.messages.create(
    to="...",
    from=" ",
    body="Yhis is my first project"
)
