from m_schema import Merchant
from datetime import datetime


new_marchant = Merchant(
    merchant_id="abcd1234",
    merchant_email='sckhoo',
    merchant_name='sckhoo',
    merchant_detail='sourdough',
    merchant_date='sourdough',
    merchant_url='khooville.com',
    merchant_socmed='sourdough',
)

print(new_marchant.merchant_socmed)
print(new_marchant.merchant_date)