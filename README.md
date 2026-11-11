E-Commerce Sales Analytics Using MySQL

Project Overview

An end-to-end E-Commerce Sales Analytics project developed using MySQL and Python. This project analyzes e-commerce business data to generate meaningful business insights through SQL queries and an interactive Streamlit dashboard.

Objectives

- Analyze overall sales and revenue performance.
- Identify top-performing products and categories.
- Understand customer purchasing behaviour.
- Evaluate seller performance.
- Track monthly sales and order trends.
- Analyze payment and shipping methods.

Technologies Used

- MySQL
- Python
- Pandas
- Streamlit
- Plotly
- MySQL Connector

Database Structure

The project contains eight relational tables:

1. Customers
2. Categories
3. Sellers
4. Products
5. Orders
6. Order Items
7. Payments
8. Shipping

SQL Analysis

The project includes SQL queries for:

- Total customers, products and orders
- Total revenue and Average Order Value (AOV)
- Monthly revenue analysis
- Top 10 products
- Category-wise revenue
- Top customers
- Seller performance
- Product profitability
- Order status analysis
- Payment method analysis
- Monthly order trends
- City-wise revenue
- Shipping status analysis
- Customer segmentation

Interactive Dashboard

The Streamlit dashboard provides visual insights into:

- Key business performance indicators
- Monthly revenue trends
- Top-selling products
- Category-wise revenue
- City-wise sales performance

Installation and Setup

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL

2. Install dependencies

pip install -r requirements.txt

3. Import the CSV files into MySQL

Create or use the "world" database and import all eight project tables.

4. Configure MySQL connection

Update the database connection settings in "sql.py" with your own MySQL host, username and password.

Do not upload database passwords or other credentials to GitHub.

5. Run the dashboard

streamlit run sql.py

Project Purpose

This project demonstrates practical SQL skills, relational database management, data analysis, Python integration and interactive business dashboard development.

Author

Developed as a portfolio project to demonstrate skills in SQL, Python and Data Analytics.
