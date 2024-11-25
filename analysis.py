# retail_analysis/analysis.py

import pandas as pd

class SuperstoreAnalysis:
    def __init__(self, data):
        """
        Initialize the SuperstoreAnalysis object.

        Parameters:
        - data (str or pd.DataFrame): Path to the dataset (CSV) or a pandas DataFrame.
        """
        if isinstance(data, str):
            # Load the dataset from a CSV file
            self.data = pd.read_csv(data)
        elif isinstance(data, pd.DataFrame):
            # Use the provided DataFrame
            self.data = data
        else:
            raise ValueError("Data must be a file path (str) or a pandas DataFrame.")


    def total_sales_by_category(self) -> pd.DataFrame:
        """
        Calculate total sales by product category.

        Returns:
        - pd.DataFrame: Total sales grouped by category.
        """
        return self.data.groupby('Category')['Sales'].sum().reset_index()

    def profit_margin_by_region(self) -> pd.DataFrame:
        """
        Calculate profit margin by region.

        Returns:
        - pd.DataFrame: Profit margin (Profit/Sales) grouped by region.
        """
        region_data = self.data.groupby('Region').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()
        region_data['Profit_Margin'] = region_data['Profit'] / region_data['Sales']
        return region_data[['Region', 'Profit_Margin']]

    def top_customers_by_sales(self, n: int = 5) -> pd.DataFrame:
        """
        Identify top N customers by total sales.

        Parameters:
        - n (int): Number of top customers to retrieve (default: 5).

        Returns:
        - pd.DataFrame: Top N customers ranked by sales.
        """
        customer_sales = self.data.groupby('Customer Name')['Sales'].sum().reset_index()
        return customer_sales.sort_values(by='Sales', ascending=False).head(n)

    def monthly_sales_trend(self) -> pd.DataFrame:
        """
        Analyze the monthly sales trend over time.

        Returns:
        - pd.DataFrame: Monthly sales trend.
        """
        self.data['Order Date'] = pd.to_datetime(self.data['Order Date'])
        self.data['Month'] = self.data['Order Date'].dt.to_period('M')
        monthly_sales = self.data.groupby('Month')['Sales'].sum().reset_index()
        monthly_sales['Month'] = monthly_sales['Month'].astype(str)
        return monthly_sales

    def segment_analysis(self) -> pd.DataFrame:
        """
        Perform sales and profit analysis by customer segment.

        Returns:
        - pd.DataFrame: Sales and profit grouped by segment.
        """
        return self.data.groupby('Segment').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()
