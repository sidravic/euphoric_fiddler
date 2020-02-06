from .query import reviews

# def get_staff_context(other_data):
#     context_data_values = other_data.get('context_data_values', {})
#     staff_context =  context_data_values.get('StaffContext', {})
#     return staff_context.get('Value', None)

# def get_verified_purchaser(other_data):
#     context_data_values = other_data.get('context_data_values', {})
#     verified_purchaser =  context_data_values.get('VerifiedPurchaser', {})
#     return verified_purchaser.get('Value', None)

# def get_skin_concerns(other_data):
#     context_data_values = other_data.get('context_data_values', {})
#     skin_concern =  context_data_values.get('skinConcerns', {})
#     return skin_concern.get('Value', None)

# def get_skin_types(other_data):
#     context_data_values = other_data.get('context_data_values', {})
#     skin_types =  context_data_values.get('skinType', {})
#     return skin_types.get('Value', None)

# def get_incentivized(other_data):
#     context_data_values = other_data.get('context_data_values', {})
#     incentivized =  context_data_values.get('IncentivizedReview', {})
#     return incentivized.get('Value', None)

# def get_hair_condition(other_data):
#     context_data_values = other_data.get('context_data_values', {})
#     hair_condition =  context_data_values.get('hairCondition', {})
#     return hair_condition.get('Value', None)

# def get_hair_color(other_data):
#     context_data_values = other_data.get('context_data_values', {})
#     hair_color =  context_data_values.get('hairColor', {})
#     return hair_color.get('Value', None)

# def get_beauty_insider(other_data):
#     context_data_values = other_data.get('context_data_values', {})
#     beauty_insider =  context_data_values.get('beautyInsider', {})
#     return beauty_insider.get('Value', None)

# def get_skin_token(other_data):
#     context_data_values = other_data.get('context_data_values', {})
#     skin_tone =  context_data_values.get('skinTone', {})
#     return skin_tone.get('Value', None)

# def get_age(other_data):
#     context_data_values = other_data.get('context_data_values', {})
#     age =  context_data_values.get('age', {})
#     return age.get('Value', None)

# def get_eye_color(other_data):
#     context_data_values = other_data.get('context_data_values', {})
#     eye_color =  context_data_values.get('eyeColor', {})
#     return eye_color.get('Value', None)

# def get_hair_concerns(other_data):
#     context_data_values = other_data.get('context_data_values', {})
#     hair_concern =  context_data_values.get('hairConcerns', {})
#     return hair_concern.get('Value', None)

CONTEXT_ATTRIBUTES = ['StaffContext',
                      'VerifiedPurchaser',
                      'skinConcerns',
                      'skinType',
                      'IncentivizedReview',
                      'hairCondition',
                      'hairColor',
                      'beautyInsider',
                      'skinTone',
                      'age',
                      'eyeColor',
                      'hairConcerns']


def get_context(other_data_row, context_attribute):
    context_data_values = other_data_row.get('context_data_values', {})
    attribute_data = context_data_values.get(context_attribute, {})
    return attribute_data.get('Value', None)


def fetch_context_attributes(copy_reviews_df):
    other_data_df = copy_reviews_df['other_data']

    for attribute in CONTEXT_ATTRIBUTES:
        context_attribute_series = other_data_df.apply(
            lambda x: get_context(x, attribute))
        print(f'Attribute: {attribute}: values: {context_attribute_series}')
        copy_reviews_df[attribute] = context_attribute_series

    return copy_reviews_df


def extract_context_attributes():
    reviews_df = reviews()
    copy_reviews_df = reviews_df.copy()
    fetch_context_attributes(copy_reviews_df)

    del copy_reviews_df['other_data']
    return copy_reviews_df

# r = extract_context_attributes()
# write_to_csv(r)
