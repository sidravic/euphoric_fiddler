from .query import WithPandas
from .urls import ImageUrlFileGenerator

BASE_DIR = '/home/sidravic/downloaded_images/internal_v3'

if __name__ == '__main__':
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

    processor_func = ImageUrlFileGenerator(BASE_DIR).generate_url_txt_file
    WithPandas().find_in_batches(query, processor_fn=processor_func)