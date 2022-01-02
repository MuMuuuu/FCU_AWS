#!/usr/bin/python3

from typing import List
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from io import BytesIO
from base64 import b64encode as b64e
import json
from fastapi import APIRouter, Depends, Path
from auth import LoginState
import models
import auth
from main import db

router = APIRouter(prefix="/store")


@router.get("/{store}/qrcode")
def get_store_qrcode(store: str = Path(...)):
    qr = qrcode.QRCode(
        border=6,
        error_correction=ERROR_CORRECT_H,
        box_size=3,
        mask_pattern=5,
    )
    buffer = BytesIO()

    qr.add_data(json.dumps({"store": store}))
    qr.make(fit=True)
    img = qr.make_image()
    img.save(buffer)

    qrbase = b64e(buffer.getvalue()).decode()

    return "data:image/png;base64,{}".format(qrbase)


@router.get("/{store}/history", response_model=List[models.StoreLocation])
async def get_store_history(store: str = Path(...), login_state: LoginState = Depends(auth.get_login_state)):
    return await db.get_store_locations(store)


@router.post("/{store}/report", response_model=models.BasicResponse)
async def post_store_report(store: str = Path(...),login_state: LoginState = Depends(auth.get_login_state)):
    await db.update_user_location(login_state.username, store)

    return {"status": 200}