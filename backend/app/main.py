from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .sms_service import send_sms

from .database import Base, engine

Base.metadata.create_all(bind=engine)

from .api import router

app = FastAPI(title='SMS Reminder Backend')
app.include_router(router)


class TestSmsRequest(BaseModel):
    to: str
    message: str = 'Test SMS from SMS-reminder MVP'


@app.get('/')
def read_root():
    return {'status': 'ok', 'message': 'SMS Reminder backend is running'}


@app.post('/test-sms')
def test_sms(payload: TestSmsRequest):
    """
    Test SMS sending.

    Example body:
    {
      "to": "+15551234567",
      "message": "Hello from my SMS reminder app!"
    }
    """
    try:
        sid = send_sms(to=payload.to, body=payload.message)
        return {'success': True, 'message_sid': sid}
    except Exception as e:
        # In real code you'd log this
        raise HTTPException(status_code=500, detail=str(e))
