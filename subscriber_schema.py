from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class Subscriber(BaseModel):
    subscriber_id : str
    subscriber_name : str
    subscriber_detail : str
    subscriber_email : EmailStr
    subscriber_url : Optional[str]
    subscriber_socmed : Optional[list]
    subscriber_date : datetime

    @classmethod
    def add(cls, subscriber_record):
        # calculate age an set it as a age
        # return new object
        return f"add received {subscriber_record}"
    
    @classmethod
    def search_by_id(cls, subscriber_id):
        # calculate age an set it as a age
        # return new object
        return f"search_by_id received {subscriber_id}"
    
    @classmethod
    def modify_by_id(cls, subscriber_to_modify):
        # calculate age an set it as a age
        # return new object
        return f"modify_by_id received {subscriber_to_modify}"
    
    @classmethod
    def suspend_by_id(cls, subscriber_id):
        # calculate age an set it as a age
        # return new object
        return f"suspend_by_id received {subscriber_id}"
    
    @classmethod
    def delete_by_id(cls, subscriber_id):
        # calculate age an set it as a age
        # return new object
        return f"delete_by_id received {subscriber_id}"