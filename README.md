# Sales Analysis Dashboard

## Project Information

* **Project Name:** Sales Analysis Dashboard
* **Student Name:** Anubhav Yadav
* **UID:** 25MCD10057
* **Course:** MCA Data Science (DS)
* **Department:** Computer Application, UIC (University Institute of Computing)
* **Subject:** Python Programming (25CAH-606)
* **Semester:** 1st Year, 1st Semester

## Project Overview

This project focuses on analyzing and visualizing sales data from the Sample Superstore dataset using Python libraries such as NumPy, Pandas, Matplotlib, Seaborn, and Streamlit. The primary objective is to create a comprehensive and interactive dashboard that allows users to explore sales trends, regional performance, category analysis, top products/customers, and profitability.

## Dataset

* **Dataset Used:** Sample Superstore Dataset (from Kaggle)
* **Columns:** Ship Mode, Segment, Country, City, State, Postal Code, Region, Category, Sub-Category, Sales, Quantity, Discount, Profit, Profit Margin (%)
* **Description:** The dataset contains sales records, including details of the shipping method, customer segment, location, product category, and numeric sales, profit, and quantity values.

## Features Implemented

1. **Data Handling and Cleaning:**

   * Removed missing values and duplicates.
   * Converted numeric columns to proper data types.
   * Handled negative sales and profit values.
   * Calculated Profit Margin (%) using NumPy.

2. **Sales Analysis:**

   * Overall metrics: total sales, total profit, average sale, average profit, total quantity.
   * Regional performance analysis.
   * Category-wise and segment-wise sales analysis.
   * Identification of top products and customers.
   * Profitability and correlation analysis.

3. **Data Visualizations:**

   * Bar Plot: Sales by Region.
   * Pie Chart: Sales distribution by Category.
   * Horizontal Bar Plot: Quantity sold per Sub-Category.
   * Scatter Plot: Sales vs Profit by Category.
   * Box Plot: Profit distribution by Category.
   * Correlation Heatmap of numerical features.
   * Pair Plot: Sales, Profit, Quantity by Category.
   * Count Plot: Orders by Ship Mode.
   * Stacked Bar Plot: Sales by Region and Category.
   * Histogram: Distribution of Profit Margin (%).

4. **Interactive Streamlit Dashboard:**

   * Sidebar filters for Region, Category, and Segment.
   * Dynamic display of filtered dataset.
   * Interactive plots and metrics update based on user selection.

## Tools and Libraries

* Python 3.12
* Libraries: NumPy, Pandas, Matplotlib, Seaborn, Streamlit

## Instructions to Run

1. Ensure Python and necessary libraries are installed:

   ```bash
   pip install numpy pandas matplotlib seaborn streamlit
   ```
2. Place the dataset `SampleSuperstore.csv` in the project directory.
3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```
4. Use sidebar filters to interact with the dashboard and explore sales data.

## Conclusions

* The analysis highlights top-performing regions, categories, and customer segments.
* Visualizations provide insights into sales trends, profitability, and product performance.
* The dashboard allows interactive exploration for better decision-making.

## Author

**Anubhav Yadav**

* UID: 25MCD10057
* MCA DS Student, Department of Computer Application, UIC (University Institute of Computing), Chandigarh University
* Python Programming, 1st Semester, 1st Year