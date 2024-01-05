from merchant_schema import Merchant
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


# new_marchant = Merchant(
#     merchant_id="abcd1234",
#     merchant_email='sckhoo@gmail.com',
#     merchant_name='sckhoo',
#     merchant_detail='sourdough',
#     merchant_date=datetime.today(),
#     merchant_url='khooville.com',
#     merchant_socmed=['twitter.com/sckhoo', 'instagram/sckhoo', 'facebook.com/sckhoo']
# )