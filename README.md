# Sales Performance Analytics

Business analytics project combining Python and SQL to evaluate product performance, revenue trends, units sold, and average order value.

## Business Questions
- Which products generate the most revenue?
- Which products sell the most units?
- How does revenue change by month?
- What is the average order value?

## Tech Stack
Python, Pandas, SQL, Power BI-ready datasets

## Structure
```text
src/sales_analysis.py       # data preparation and KPI aggregation
sql/business_queries.sql    # reusable business SQL queries
```

## Data Model
Expected fields include `order_id`, `order_date`, `product`, `quantity`, and `unit_price`. Revenue is calculated as `quantity * unit_price`.

## Python Usage
```python
import pandas as pd
from src.sales_analysis import product_performance

df = pd.read_csv("sales.csv")
print(product_performance(df).head(10))
```

## SQL Analysis
The SQL folder contains examples for product revenue, monthly trends, and average order value.

## Next Steps
Add customer segmentation, regional analysis, interactive Power BI pages, automated tests, and a documented sample dataset.