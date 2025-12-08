from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .database import SessionLocal
from . import crud, schemas

router = APIRouter()

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
    