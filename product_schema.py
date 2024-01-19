from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class Product(BaseModel):
    product_id : str
    product_name : str
    product_detail : str
    product_date : datetime
    product_freq : int
    product_freq_unit : str

    @classmethod
    def add(cls, product_record):
        # calculate age an set it as a age
        # return new object
        return f"add received {product_record}"
    
    @classmethod
    def search_by_id(cls, product_id):
        # calculate age an set it as a age
        # return new object
        return f"search_by_id received {product_id}"
    
    @classmethod
    def modify_by_id(cls, product_to_modify):
        # calculate age an set it as a age
        # return new object
        return f"modify_by_id received {product_to_modify}"
    
    @classmethod
    def suspend_by_id(cls, product_id):
        # calculate age an set it as a age
        # return new object
        return f"suspend_by_id received {product_id}"
    
    @classmethod
    def delete_by_id(cls, product_id):
        # calculate age an set it as a age
        # return new object
        return f"delete_by_id received {product_id}"