
# Amazon Pricing Strategy Analysis
## 🎯 Business Problem

"Is our discounting strategy effective, or are we leaving money on the table and training customers to wait for sales?"


## 📊 Analysis Notebooks

### 🔍 Data Understanding & Cleaning
[![Open in nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/bykov-make/amazon-pricing-strategy/blob/main/analysis/1_data_understanding.ipynb)

**View the interactive analysis:**

- **[Data Understanding Notebook](https://nbviewer.org/github/bykov-make/amazon-pricing-strategy/blob/main/analysis/1_data_understanding.ipynb)** - Complete data cleaning and initial insights

## 📈 Quick Status

- **Data**: ✅ 1,465 products cleaned and validated
- **Analysis**: 🔄 In progress
- **Dashboard**: 🚧 Planned

## 📊 Key Findings (Initial)

- **Dataset**: 1,465 products across multiple categories
- **Pricing Strategy**: 47.7% average discount rate industry-wide
- **Customer Response**: 4.1/5 average rating suggests discount effectiveness
- **Data Quality**: Robust pipeline handling Indian rupee formatting (₹) and comma separators

## 🛠️ Technical Highlights

```python

# Config-driven cleaning pipeline

CLEANING_CONFIG = {

'currency_columns': {

'discounted_price': 'discounted_price_clean',

'actual_price': 'actual_price_clean'

},

'percentage_columns': {

'discount_percentage': 'discount_percent_clean'

}

}
```


## 🎯 Next Phase Analysis

- **Discount Efficiency:** ROI analysis of discount depth vs. sales volume
- **Product Segmentation:** 2x2 matrix (Discount % vs. Rating Count)
- **Strategic Categories:** Identify over-discounted vs. under-discounted segments
- **Actionable Insights:** Data-driven discount optimization recommendations
  

## 📁 Project Structure

  ```text
amazon-pricing-strategy/

├── analysis/

│ ├── 1_data_understanding.ipynb

│ └── 2_pricing_segmentation.ipynb (planned)

├── data/

│ └── amazon.csv

├── environment.yml

├── .gitignore

└── README.md
```

  
## 🤝 Contributing

Questions or suggestions? Please open an issue or reach out to discuss pricing strategy insights!

## 📄 License

MIT License - feel free to use this analysis approach in your own projects.

## 📫 Contact

- **Maintained by**: Me 😁

- **Project**: Amazon Pricing Strategy Analysis

- **Status**: Active Development
