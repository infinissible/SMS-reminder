from sqlalchemy.orm import Session
from . import models, schemas

def create_appointment(db: Session, data: schemas.AppointmentCreate):
    appointment = models.Appointment(
        customer_name=data.customer_name,
        phone=data.phone,
        appointment_time=data.appointment_time,
        remind_before_minutes=data.remind_before_minute,
    )
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment

def get_appointments(db: Session):
    return db.query(models.Appointment).all()