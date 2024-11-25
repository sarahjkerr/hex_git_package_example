# hex_git_package_example
An example repository for importing an existing python script into a Hex project using git packages

## Examples
from retail_analysis import SuperstoreAnalysis

### Initialize with the file path to the dataset
analyzer = SuperstoreAnalysis("SampleSuperstore.csv")

### 1. Get total sales by category
print(analyzer.total_sales_by_category())

### 2. Calculate profit margins by region
print(analyzer.profit_margin_by_region())

### 3. Top 5 customers by sales
print(analyzer.top_customers_by_sales(n=5))

### 4. Monthly sales trend
print(analyzer.monthly_sales_trend())

### 5. Sales and profit by customer segment
print(analyzer.segment_analysis())
