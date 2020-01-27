import os
from sqlalchemy import create_engine
import pandas as pd
import html

db_string = os.environ['DB_URL']
engine = create_engine(db_string)
db_conn = engine.connect()


def from_row_proxy_to_dict(row_proxy):
    return {k: v for k, v in row_proxy.items()}


def from_result_proxy_to_result_batch(result_proxy):
    result_batch = []
    for row_proxy in result_proxy:
        row = from_row_proxy_to_dict(row_proxy)
        result_batch.append(row)
    return result_batch


def next_limit(offset, max_records, current_batch_limit):
    next_fetch_eval = max_records - (offset + current_batch_limit)
    if next_fetch_eval >= 0:
        return current_batch_limit
    elif next_fetch_eval < 0:
        return abs(next_fetch_eval)


class WithSql():
    """
    WithSql().find_in_batches(query, processor_fn=processor_fn, max_records=250)
    """

    def __init__(self):
        self.db_conn = db_conn
        self.db_string = db_string

    def get_total_query_count(self, query):
        query = f'select COUNT(*) from ( {query} ) as count_query'
        result = self.db_conn.execute(query).scalar()
        return result

    def find_in_batches(self, query, processor_fn=None, limit=None, max_records=None):
        offset = 0

        if not max_records:
            max_records = self.get_total_query_count(f'select DISTINCT on (cp.name) cp.id from cosmetics_products cp')

        if not limit:
            limit = 100

        while offset <= max_records:
            print(f'From: {offset}. to {offset + limit}')
            query_with_offsets = f'{query} OFFSET {offset} LIMIT {limit}'
            result_set = db_conn.execute(query_with_offsets)
            result_batch = from_result_proxy_to_result_batch(result_proxy=result_set)

            if processor_fn:
                processor_fn(result_batch)

            offset += result_set.rowcount
            limit = next_limit(offset, max_records, limit)


class WithPandas():
    """
    WithPandas().find_in_batches(query, processor_fn=processor_fn)
    """

    def __init__(self):
        self.db_conn = db_conn

    def find_in_batches(self, query, processor_fn=None):
        df = pd.read_sql_query(query, con=self.db_conn, chunksize=100)

        for chunk in df:
            grouped_df = chunk.groupby(by='product_id')

            for product_id, attributes in grouped_df:
                product_name = html.unescape(attributes['product_name'].unique()[0])
                brand_name = html.unescape(attributes['brand_name'].unique()[0])
                image_urls = attributes['image_url'].unique()

                if processor_fn:
                    processor_fn(product_id, image_urls, product_name, brand_name)


query = '''
SELECT unique_products.*, ci.image_url, ci.s3_image_url, ci.source
                         from (
                                  SELECT DISTINCT ON (cp.name) cp.name as product_name,
                                                               cb.name as brand_name,
                                                               cp.id   as product_id,
                                                               cb.id   as brand_id
                                  from cosmetics_products cp
                                           inner join cosmetics_brands cb on cp.cosmetics_brand_id = cb.id
                                  order by cp.name asc, cb.name asc) unique_products
                                  INNER JOIN cosmetics_images ci on ci.cosmetics_product_id = product_id
                         ORDER BY unique_products.product_name ASC, unique_products.brand_name ASC
'''


