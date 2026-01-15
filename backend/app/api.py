from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from .database import SessionLocal
from . import crud, schemas
from .sms_service import send_sms

router = APIRouter()


# -------------------------
# Appointment endpoints
# -------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/appointments', response_model=schemas.AppointmentResponse)
def create_appointment_endpoint(data: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    return crud.create_appointment(db, data)


@router.get('/appointments')
def list_appointments(db: Session = Depends(get_db)):
    return crud.get_appointments(db)


# -------------------------
# SMS test endpoint
# -------------------------
class TestSMSRequest(BaseModel):
    to: str
    message: str = 'Test SMS from SMS-reminder MVP'


@router.post(
    '/test-sms',
    summary='Send a test SMS',
)
def test_sms(payload: TestSMSRequest):
    """
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
        raise HTTPException(status_code=500, detail=str(e))
