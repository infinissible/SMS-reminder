from twilio.rest import Client
from .config import settings

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

def send_sms(to: str, body: str) -> str:
    """
    Send an SMS using Twilio.
    Returns the Twilio message SID if successful.
    """
    # if not settings.TWILIO_ACCOUNT_SID or not settings.TWILIO_AUTH_TOKEN or not settings.TWILIO_FROM_NUMBER:
    #     raise RuntimeError('Twilio settings are not configured. Check your .env file.')

    # message = client.messages.create(
    #     body=body,
    #     from_=settings.TWILIO_FROM_NUMBER,
    #     to=to,
    # ) 
    # return message.sid
    print(f"[FAKE SMS] to={to} body={body}")
    return "FAKE-SID-12345"