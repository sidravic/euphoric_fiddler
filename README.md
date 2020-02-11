## Valuable Links 

1. Count and sort with Pandas https://stackoverflow.com/questions/40454030/count-and-sort-with-pandas
2. Using `isin` for selecting from a list https://stackoverflow.com/questions/40454030/count-and-sort-with-pandas


### Topics

1. Collaborative filtering with Fastai https://towardsdatascience.com/collaborative-filtering-with-fastai-3dbdd4ef4f00

## Valuable snippets

### Dropping duplicates
```python
dedup_df = without_reviews_df.drop_duplicates(
                                   subset=['product_id', 'user_nickname', 'review_text'], 
                                   keep='first', 
                                   inplace=False)
dedup_df
```

### Group by

```python
grouped_by_category_df = dedup_df.groupby(by='product_category_primary')
grouped_by_category_df
```

### Group by `user_nickname` in sorted order and `count` the number of products in each group and return `nlargest` groups

```python
x = (relevant_makeup_df.groupby(by=['user_nickname'], sort=True)['product']
                  .count()
                  .nlargest(38679))
```

### Find percentage of missing values in the dataset

1. `relevant_makeup_df.isna().sum()` Finds the all the `nan` or `null` values in the dataset for each column
    and sums it up
2.  `relevant_makeup_df.shape[0]` Fetches the number of rows in the dataset and divides the result of 1 and multiples by 100 to make it percentage
```python
relevant_makeup_df.isna().sum()/relevant_makeup_df.shape[0] * 100
```

### Find and assign all not null values to a dataframe for a specific column

```python
# For each group - in this case for user `Mochapj`
d = grouped_by_user_df.get_group('Mochapj')

# Find all the `skinConcerns` that are not null
skin_concerns_df = d[d['skinConcerns'].notnull()]

# Fetch the unique value if only one
skin_concerns_df['skinConcerns'].unique()[0]

# select all records from `relevant_make_df` for the user `Mochapj` and assign the attribute `skinConcerns` with the value `aging`
relevant_makeup_df.loc[relevant_makeup_df['user_nickname']=='Mochapj', 'skinConcerns'] = 'aging'

# List and view the updated values
relevant_makeup_df.loc[relevant_makeup_df['user_nickname']=='Mochapj']
```

### Drop `na` values for a specific column in a dataframe

```python
df.dropna(subset=['EPS'], how='all', inplace=True)
```