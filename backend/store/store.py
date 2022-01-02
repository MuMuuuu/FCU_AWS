#!/usr/bin/python3

import qrcode
from qrcode.constants import ERROR_CORRECT_H
from io import BytesIO
from base64 import b64encode as b64e
import json
from fastapi import APIRouter
import models

router = APIRouter()

@router.get("/{store}/qrcode")
def qrcode_gen(store: str):
    qr = qrcode.QRCode(
        border=6,
        error_correction=ERROR_CORRECT_H,
        box_size=3,
        mask_pattern=5,
    )
    buffer = BytesIO()
    
    qr.add_data(json.dumps({"store_name": store}))
    qr.make(fit=True)
    img = qr.make_image()
    img.save(buffer)

    qrbase = b64e(buffer.getvalue()).decode()

    return "data:image/png;base64,{}".format(qrbase)

@router.get("/{store}/list" , response_model=models.Verify)
async def get_list(store: str):
    try:
        result = jwt.decode(store , key=JWT_KEY , algorithm=JWT_ALG)
    except JwtDecodeError:
        return HTTPException("403" , "JWT DecodeError")
    
    return await self.find_one({"location" : store})

