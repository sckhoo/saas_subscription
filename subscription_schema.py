from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Subscription(BaseModel):
    subscription_id : str
    subscriber_id : str
    merchant_id : str
    subscription_start : datetime
    subscription_end : Optional[datetime]
    subscription_freq : int
    subscription_freq_unit : str

    @classmethod
    def add(cls, subscription_record):
        # calculate age an set it as a age
        # return new object
        return f"add received {subscription_record}"
    
    @classmethod
    def search_by_id(cls, subscription_id):
        # calculate age an set it as a age
        # return new object
        return f"search_by_id received {subscription_id}"
    
    @classmethod
    def modify_by_id(cls, subscription_to_modify):
        # calculate age an set it as a age
        # return new object
        return f"modify_by_id received {subscription_to_modify}"
    
    @classmethod
    def suspend_by_id(cls, subscription_id):
        # calculate age an set it as a age
        # return new object
        return f"suspend_by_id received {subscription_id}"
    
    @classmethod
    def delete_by_id(cls, subscription_id):
        # calculate age an set it as a age
        # return new object
        return f"delete_by_id received {subscription_id}"