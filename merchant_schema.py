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

    @classmethod
    def add(cls, merchant_record):
        # calculate age an set it as a age
        # return new object
        return f"add received {merchant_record}"
    
    @classmethod
    def search_by_id(cls, merchant_id):
        # calculate age an set it as a age
        # return new object
        return f"search_by_id received {merchant_id}"
    
    @classmethod
    def modify_by_id(cls, merchant_to_modify):
        # calculate age an set it as a age
        # return new object
        return f"modify_by_id received {merchant_to_modify}"
    
    @classmethod
    def suspend_by_id(cls, merchant_id):
        # calculate age an set it as a age
        # return new object
        return f"suspend_by_id received {merchant_id}"
    
    @classmethod
    def delete_by_id(cls, merchant_id):
        # calculate age an set it as a age
        # return new object
        return f"delete_by_id received {merchant_id}"