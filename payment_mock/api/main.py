from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from payment_mock.api.endpoints.health import router as health_router
from payment_mock.api.endpoints.payment_mock import router as prescriptions_router


def create_app():
    app = FastAPI(title="Partner Payment Mock")


    # Middlewares
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Define routers
    app.include_router(health_router, tags=["health"], prefix="/health")
    app.include_router(
        prescriptions_router, tags=["payment_login_mock"], prefix=""
    )

    return app


app = create_app()
