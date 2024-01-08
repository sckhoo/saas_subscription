from merchant_schema import Merchant
from product_schema import Product
from datetime import datetime


new_marchant = Merchant(
    merchant_id="abcd1234",
    merchant_email='sckhoo@gmail.com',
    merchant_name='sckhoo',
    merchant_detail='sourdough',
    merchant_date=datetime.today(),
    merchant_url='khooville.com',
    merchant_socmed=['x/sckhoo', 'fb/sckhoo'],
)

new_product = Product(
    product_id="abcd1234",
    product_name='sckhoo',
    product_detail='sourdough',
    product_date=datetime.today(),
)

print(new_marchant.merchant_socmed)
print(new_marchant.add(new_marchant.dict()))
print(new_marchant.search_by_id("khoo"))
print(new_marchant.modify_by_id(new_marchant.dict()))
print(new_marchant.suspend_by_id("id_to_be_suspended"))
print(new_marchant.delete_by_id("id_to_be_deleted"))

print(new_product.product_name)
print(new_product.add(new_product.dict()))
print(new_product.search_by_id("khoo"))
print(new_product.modify_by_id(new_product.dict()))
print(new_product.suspend_by_id("id_to_be_suspended"))
print(new_product.delete_by_id("id_to_be_deleted"))
