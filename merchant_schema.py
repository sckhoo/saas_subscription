from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from datetime import datetime

class Merchant(BaseModel):
    merchant_id : str
    merchant_name : str
    merchant_detail : str
    merchant_email : EmailStr
    merchant_url : Optional[str]
    merchant_socmed : Optional[dict]
    merchant_date : datetime

    @classmethod
    def add(cls, merchant_record):
        # calculate age an set it as a age
        # return new object
        return f"add received {merchant_record}"
    
    @validator("merchant_id")
    def validate_merchant_id(cls, merchant_id: str):
        if (len(merchant_id) == 8) and (merchant_id.isalnum()):
            return merchant_id
        else:
            print("merchant_id not right format")
            
    @classmethod
    def merchant_add(cls, new_merchant):
        # calculate age an set it as a age
        # return new object
        return cls(name, date.today().year - birth_year)
