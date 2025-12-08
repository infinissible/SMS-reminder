from pydantic import BaseModel
from datetime import datetime

class AppointmentCreate(BaseModel):
    customer_name: str
    phone: str
    appointment_time: datetime
    remind_before_minute: int = 60

class AppointmentResponse(BaseModel):
    id: int
    customer_name: str
    appointment_time: datetime
    remind_before_minutes: int
    reminder_sent: bool
    
    class Config:
        orm_mode = True
        