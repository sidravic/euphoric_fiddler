from .review_context_attributes import extract_context_attributes
from .create_csv import write_to_csv




def extract_product_categories(reviews_with_context_attr_df):
    primary_category = list()
    secondary_category = list()

    product_categories = reviews_with_context_attr_df['product_categories']
    for categorization in product_categories:
        classifications = categorization.get('classification', [])
        if len(classifications) == 0:
            primary_category.append(None)
            secondary_category.append(None)
        elif len(classifications) == 1:
            primary_category.append(classifications[0])
            secondary_category.append(None)
        elif len(classifications) == 2:
            primary_category.append(classifications[0])
            secondary_category.append(classifications[1])

    reviews_with_context_attr_df['product_category_primary'] = primary_category
    reviews_with_context_attr_df['product_category_secondary'] = secondary_category
    return reviews_with_context_attr_df



def product_categories():
    reviews_with_context_attr_df = extract_context_attributes()
    extract_product_categories(reviews_with_context_attr_df)
    print(reviews_with_context_attr_df.columns)
    print(reviews_with_context_attr_df['product_category_primary'])
    del reviews_with_context_attr_df['product_categories']
    write_to_csv(reviews_with_context_attr_df)
    return reviews_with_context_attr_df

product_categories()