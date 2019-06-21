# -*- coding: utf-8 -*-

import twilio.rest as tr

account_sid = "ACb0bd9584538498dfd6a5a8870e12a6be"
auth_token = "16b45adf0c0361a488842182fb145717"
client = tr.Client(account_sid,auth_token)
message = client.messages.create(
        body = "电脑被开机",
        from_ = "+18506953272",
        to  = "+86 18500639286"
        )
print(message.sid)
