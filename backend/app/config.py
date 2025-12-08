import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv() # looks for a file named .env in the current or parent dirs

@dataclass
class Settings:
    TWILIO_ACCOUNT_SID: str = os.environ.get("TWILIO_ACCOUNT_SID", '')
    TWILIO_AUTH_TOKEN: str = os.environ.get('TWILIO_AUTH_TOKEN', '')
    TWILIO_FROM_NUMBER: str = os.environ.get('TWILIO_FROM_NUMBER', '')
                                             
settings = Settings()                                             

