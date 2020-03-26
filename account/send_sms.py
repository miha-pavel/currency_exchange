from twilio.rest import Client


account_sid = "ACc639786317ec051064b4f63fcb6f15bc"
auth_token = "fbaa352a000e0d171f3089efb2366bc7"
client = Client(account_sid, auth_token)


def send_sms(phone, code):
    message = client.messages.create(
        to=phone,
        from_="+12018014527",
        body=f"Your activate code is {code}")
