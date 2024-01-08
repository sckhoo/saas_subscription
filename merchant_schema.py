from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from datetime import datetime

class Merchant(BaseModel):
    merchant_id : str
    merchant_name : str
    merchant_detail : str
    merchant_email : EmailStr
    merchant_url : Optional[str]
    merchant_socmed : Optional[list]
    merchant_date : datetime