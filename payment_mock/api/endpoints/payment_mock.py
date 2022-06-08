from concurrent.futures import thread
from fastapi import APIRouter
from starlette import status
import time

router = APIRouter()


@router.post("/user/login", status_code=status.HTTP_200_OK)
async def login() -> dict:
    return {"token": "token1234"}


@router.post("/multibank/transfer/", status_code=status.HTTP_200_OK)
async def login() -> dict:
    time.sleep(60)
    return {"msg": "ok"}
