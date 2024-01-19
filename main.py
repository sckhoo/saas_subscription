from merchant_schema import Merchant
from product_schema import Product
from subscriber_schema import Subscriber
from subscription_schema import Subscription

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
    product_freq=2,
    product_freq_unit='weeks',
)

new_subscriber = Subscriber(
    subscriber_id="abcd1234",
    subscriber_name='sckhoo',
    subscriber_detail='sourdough',
    subscriber_email='sckhoo@gmail.com',
    subscriber_date=datetime.today(),
    subscriber_url='khooville.com',
    subscriber_socmed=['x/sckhoo', 'fb/sckhoo'],
)

new_subscription = Subscription(
    subscription_id="subscription12345",
    subscriber_id="abcd1234",
    merchant_id="abcd1234",
    subscription_start=datetime.today(),
    subscription_end=datetime.today(),
    subscription_freq=4,
    subscription_freq_unit='week',
)

print(new_marchant.merchant_socmed)
print(new_marchant.add(new_marchant.model_dump()))
print(new_marchant.search_by_id("khoo"))
print(new_marchant.modify_by_id(new_marchant.model_dump()))
print(new_marchant.suspend_by_id("id_to_be_suspended"))
print(new_marchant.delete_by_id("id_to_be_deleted"))

print(new_product.product_name)
print(new_product.add(new_product.model_dump()))
print(new_product.search_by_id("khoo"))
print(new_product.modify_by_id(new_product.model_dump()))
print(new_product.suspend_by_id("id_to_be_suspended"))
print(new_product.delete_by_id("id_to_be_deleted"))

print(new_subscriber.subscriber_name)
print(new_subscriber.add(new_subscriber.model_dump()))
print(new_subscriber.search_by_id("khoo"))
print(new_subscriber.modify_by_id(new_subscriber.model_dump()))
print(new_subscriber.suspend_by_id("id_to_be_suspended"))
print(new_subscriber.delete_by_id("id_to_be_deleted"))

print(new_subscription.subscription_id)
print(new_subscription.add(new_subscription.model_dump()))
print(new_subscription.search_by_id("khoo"))
print(new_subscription.modify_by_id(new_subscription.model_dump()))
print(new_subscription.suspend_by_id("id_to_be_suspended"))
print(new_subscription.delete_by_id("id_to_be_deleted"))