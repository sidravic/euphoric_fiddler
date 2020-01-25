class ImageUrlFileGenerator():
    def __init__(self):
        pass

    def generate_url_txt_file(self, df):
        grouped_df = df.groupby('product_id')
        for product_id, attributes in grouped_df.items():
            print(f'ProductID: {product_id}')
            print(attributes)

        return None

