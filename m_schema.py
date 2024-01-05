from datetime import datetime

class Merchant():
    # merchant_id : str
    # merchant_name : str
    # merchant_detail : str
    # merchant_email : str
    # merchant_url : str
    # merchant_socmed : list
    # merchant_date : datetime

    def __init__(self, merchant_id, merchant_name, merchant_detail, merchant_email, merchant_url, merchant_socmed, merchant_date):
        self.merchant_id = merchant_id
        self.merchant_name = merchant_name
        self.merchant_detail = merchant_detail
        self.merchant_email = merchant_email
        self.merchant_url = merchant_url
        self.merchant_socmed = merchant_socmed
        self.merchant_date = merchant_date