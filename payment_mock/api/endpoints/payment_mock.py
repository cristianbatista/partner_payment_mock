from concurrent.futures import thread
from fastapi import APIRouter
from starlette import status
import time

router = APIRouter()


@router.post("/user/login", status_code=status.HTTP_400_BAD_REQUEST)
async def login() -> dict:
    return {"code": 103, "msg": "Faltando senha" }


@router.post("/account/transfers/ewally/", status_code=status.HTTP_200_OK)
async def login() -> dict:
    time.sleep(60)
    return {"msg": "ok"}
