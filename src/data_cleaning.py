import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(__file__))
from config import CLEANING_CONFIG

#Cleaning Logic
def clean_dataset(df , config=CLEANING_CONFIG):
    
    print("===> Cleaning Data")
    try: 
    
        df_clean = df.copy()
        print("Data frame copied successfully!", flush=True)
        
        #Clean currency columns, removing currency symbols and commas
        print("Cleaning currency symbols and removing commas")
        #sys.stdout.write("Cleaning currency symbols and removing commas \n")
        #sys.stdout.flush()
        
        for source_col, clean_col in config['currency_columns'].items():
            if source_col in df.columns:
                df_clean[clean_col] = (df[source_col].astype(str).str.replace(r'[₹$,]', '', regex=True)
                        .pipe(pd.to_numeric, errors = 'coerce'))
    
        #Clean percentage columns
        print("Cleaning percentage symbols")
        for source_col, clean_col in config['percentage_columns'].items():
            if source_col in df.columns:
                df_clean[clean_col] = (df[source_col].astype(str).str.replace('%','')
                    .pipe(pd.to_numeric, errors='coerce'))

        #Clean rating 
        print("Cleaning numeric columns")
          
        #Clean numeric columns
        for source_col, clean_col in config['numeric_columns'].items():
           if source_col in df.columns:
                df_clean[clean_col] = (df[source_col].astype(str).str.replace(',','')
                    .pipe(pd.to_numeric, errors='coerce'))
                
        print("Data Cleaned <===")
       
    except Exception as e:
        print(f"Error in clean_dataset: {e}")
        raise
    return df_clean


#Cleaning Validation.
def validate_cleaning(df_clean):
  
    print("=== Cleaning Validation ===")

    #Check Data Types.
    print("\nData Types After Cleaning:")
    clean_cols = [col for col in df_clean.columns if 'clean' in col]
    print(df_clean[clean_cols].dtypes)

    #Check Basic Stats
    print("\nBasic Stats over Clean Data:")
    print(df_clean[clean_cols].describe())

    #Before / After Comparison.
    print("Sample Before / After:" )
    sample_cols = ['discounted_price', 'discounted_price_clean', 'actual_price', 'actual_price_clean']
    print(df_clean[sample_cols].head(5))

    return df_clean[clean_cols].describe()