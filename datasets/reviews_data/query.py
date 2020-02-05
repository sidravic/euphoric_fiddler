import os
import pandas as pd
from sqlalchemy import create_engine

db_string = os.environ['DB_URL']
engine = create_engine(db_string)
db_conn = engine.connect()

valid_product_ids_query = '''
    SELECT unique_products.*
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



def extract_valid_product_ids(query):
    df = pd.read_sql_query(valid_product_ids_query, con=db_conn)
    product_id_df = df['product_id']
    unique_product_ids = product_id_df.unique()
    return unique_product_ids

def reviews_query(product_ids_as_str):
    return f"""
        select cp.id as product_id, cp.name as product, cb.name as brand, crc.* as review  from cosmetics_review_comments crc 
            INNER JOIN cosmetics_reviews cr ON crc.cosmetics_review_id = cr.id
            INNER JOIN cosmetics_products cp ON cr.cosmetics_product_id = cp.id
            INNER JOIN cosmetics_brands cb ON cp.cosmetics_brand_id = cb.id
        WHERE cp.id IN ({product_ids_as_str})
    """

def fetch_reviews(query, chunksize=None):
    return pd.read_sql_query(query, con=db_conn, chunksize=chunksize)

def reviews():
    valid_product_ids = extract_valid_product_ids(valid_product_ids_query)
    product_uuids = valid_product_ids.tolist()
    product_ids = [f"'{product_id.__str__()}'" for product_id in product_uuids]
    product_ids_as_string = ','.join(product_ids)
    reviews_query_string = reviews_query(product_ids_as_string)
    reviews_df = fetch_reviews(reviews_query_string)
    return reviews_df

