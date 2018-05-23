from __future__ import print_function
from bl_db_product_amz_best.products import Products
from pprint import pprint

api_instance = Products()

try:
    offset = 0
    limit = 100

    while True:
        res = api_instance.get_products_by_node_id(node_id='aaaa', offset=offset, limit=limit)

        if limit > len(res):
            break
        else:
            offset = offset + limit

    pprint(res)

except Exception as e:
    print("Exception when calling get_products_by_node_id: %s\n" % e)