#Data Cleaning Configuration

CLEANING_CONFIG = {
    'currency_columns' : {
        'discounted_price' : 'discounted_price_clean',
        'actual_price' : 'actual_price_clean'
    },
    'percentage_columns' : {
        'discount_percentage' : 'discount_percent_clean'
    },
    'numeric_columns' : {
        'rating_count' : 'rating_count_clean',
        'rating': 'rating_clean'
    }
 }