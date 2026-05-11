# Ch. 2 End-to-End Machine Learning Project

Predict a CA district's median house price given Census data:

- population
- median income
- median house price/district

## Framework

- Training type: **Supervised**
- Problem type: **Multiple regression** (use multiple features -> prediction)
  - univariate regression problem (predict a single value)
- Learning type: **Batch**
- Performance measurement: **Root mean square**

## Data exploration notes

- `total_bedrooms` is missing data: 20433/20640
- `median_income` is in ten thousand and capped >= 5 and <= 15
- `housing_median_age` capped (?) 
- `median_house_value` capped <= 500,000
- many histograms *skewed right* (farther right of the median than to the left)
