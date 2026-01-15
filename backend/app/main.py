from .database import Base, engine
from .app import create_app

Base.metadata.create_all(bind=engine)

app = create_app()
