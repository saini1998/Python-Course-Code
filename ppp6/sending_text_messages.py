# SENDING TEXT MESSAGES
# twillio api

# +17209244281
from twillio.rest import Client
account_sid = "AC7aecc32e7572f636725904e390245431"
auth_token = "79be12fec2409db0422c72a9b16d72f0"
client = Client(account_sid, auth_token)

call = client.messages.create(
    to="...",
    from=" ",
    body="Yhis is my first project"
)
