from fastapi import FastAPI
from .api import router


def create_app():
    app = FastAPI(title='SMS Reminder Backend')
    app.include_router(router)

    @app.get('/')
    def read_root():
        return {'status': 'ok', 'message': 'SMS Reminder backend is runnig'}

    return app
