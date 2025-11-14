
# Amazon Pricing Strategy Analysis
## 🎯 Analytical Objective

Explore Amazon's pricing landscape to understand market discount patterns and identify data-driven opportunities for future analysis.

*Note: Dataset limitations prevent conclusive pricing strategy recommendations, but provide valuable market insights.

## 📊 Analysis Notebooks

### 🔍 Data Understanding & Cleaning
[![Open in nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/bykov-make/amazon-pricing-strategy/blob/main/analysis/1_data_understanding.ipynb)

**View the interactive analysis:**

- **[Data Understanding Notebook](https://nbviewer.org/github/bykov-make/amazon-pricing-strategy/blob/main/analysis/1_data_understanding.ipynb)** - Complete data cleaning and initial insights

## 📈 Exploratory Market Analysis.

- **[Links to be added]**

## 📈 Project Status

- **Data Engineering**: ✅ 1,465 products cleaned and validated
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



## 📁 Project Structure

  ```text
amazon-pricing-strategy/
├── analysis/
│   ├── 1_data_understanding.ipynb
│   └── 2_exploratory_analysis.ipynb
├── src/
│   ├── data_cleaning.py
│   └── config.py
├── data/
│   └── amazon.csv
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
