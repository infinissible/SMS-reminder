from sqlalchemy import Column, Integer, String, DateTime, Boolean
from .database import Base


class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    appointment_time = Column(DateTime, nullable=False)
    remind_before_minutes = Column(Integer, default=60)
    reminder_sent = Column(Boolean, default=False)
