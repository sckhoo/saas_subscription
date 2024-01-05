from merchant_schema import Merchant
from datetime import datetime


new_marchant = Merchant(
    merchant_id="abcd1234",
    merchant_email='sckhoo@gmail.com',
    merchant_name='sckhoo',
    merchant_detail='sourdough',
    merchant_date=datetime.today(),
    merchant_url='khooville.com',
    merchant_socmed=['x/sckhoo', 'ig/sckhoo', 'fb/sckhoo']
)

print(new_marchant.merchant_socmed)


