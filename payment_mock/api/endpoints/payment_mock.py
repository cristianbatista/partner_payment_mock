from concurrent.futures import thread
from fastapi import APIRouter
from starlette import status
import time

router = APIRouter()


@router.post("/user/login", status_code=status.HTTP_200_OK)
async def login() -> dict:
    return {"token": "token1234" }


@router.post("/account/transfers/ewally/", status_code=status.HTTP_429_TOO_MANY_REQUESTS)
async def login() -> dict:
    return {"error": "internal error"}
