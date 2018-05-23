from __future__ import print_function
from bl_db_product_amz_best.products import Products
from pprint import pprint

api_instance = Products()

product = {}
product['NodeId'] = 'aNodeId'
product['Title'] = 'aTitle'
product['ASIN'] = 'anAsin'
product['DetailPageURL'] = None
product['Binding'] = 'aBinding'

try:
    res = api_instance.add_product(product=product)
    pprint(res)

except Exception as e:
    print("Exception when calling add_product: %s\n" % e)