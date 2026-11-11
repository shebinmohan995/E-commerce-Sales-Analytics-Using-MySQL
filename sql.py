import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="E-Commerce Analytics",
    layout="wide"
)

st.title("E-Commerce Business Intelligence")
st.caption("Sales Analytics Dashboard")

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="NewPassword",
        database="world",
        connection_timeout=10,
        autocommit=True
    )

def fetch_data(query):
    connection = get_connection()
    try:
        return pd.read_sql(query, connection)
    finally:
        connection.close()

try:

    st.success("MySQL Database Connected Successfully")

    # KPI DATA
    customers = fetch_data(
        "SELECT COUNT(*) AS total FROM customers"
    )

    products = fetch_data(
        "SELECT COUNT(*) AS total FROM products"
    )

    orders = fetch_data(
        "SELECT COUNT(*) AS total FROM orders"
    )

    revenue = fetch_data(
        "SELECT SUM(line_total) AS total FROM order_items"
    )

    total_customers = customers.iloc[0, 0]
    total_products = products.iloc[0, 0]
    total_orders = orders.iloc[0, 0]
    total_revenue = revenue.iloc[0, 0] or 0

    # KPI CARDS
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Customers", f"{total_customers:,}")
    col2.metric("Total Products", f"{total_products:,}")
    col3.metric("Total Orders", f"{total_orders:,}")
    col4.metric("Total Revenue", f"₹{total_revenue:,.2f}")

    st.divider()

    # MONTHLY REVENUE
    st.subheader("Monthly Revenue")

    monthly = fetch_data("""
        SELECT
            DATE_FORMAT(o.order_date, '%Y-%m') AS month,
            SUM(oi.line_total) AS revenue
        FROM orders o
        JOIN order_items oi
            ON o.order_id = oi.order_id
        GROUP BY month
        ORDER BY month
    """)

    fig1 = px.line(
        monthly,
        x="month",
        y="revenue",
        markers=True,
    )

    st.plotly_chart(fig1, use_container_width=True)

    # TOP PRODUCTS
    st.subheader("Top 10 Best-Selling Products")

    top_products = fetch_data("""
        SELECT
            p.product_name,
            SUM(oi.quantity) AS total_sold
        FROM products p
        JOIN order_items oi
            ON p.product_id = oi.product_id
        GROUP BY p.product_id, p.product_name
        ORDER BY total_sold DESC
        LIMIT 10
    """)

    fig2 = px.bar(
        top_products,
        x="product_name",
        y="total_sold",
    )

    st.plotly_chart(fig2, use_container_width=True)

    # CATEGORY REVENUE
    st.subheader("Category-wise Revenue")

    category = fetch_data("""
        SELECT
            c.category_name,
            SUM(oi.line_total) AS revenue
        FROM categories c
        JOIN products p
            ON c.category_id = p.category_id
        JOIN order_items oi
            ON p.product_id = oi.product_id
        GROUP BY c.category_id, c.category_name
        ORDER BY revenue DESC
    """)

    fig3 = px.pie(
        category,
        names="category_name",
        values="revenue",
    )

    st.plotly_chart(fig3, use_container_width=True)

    # CITY REVENUE
    st.subheader("City-wise Revenue")

    city = fetch_data("""
        SELECT
            c.city,
            SUM(oi.line_total) AS revenue
        FROM customers c
        JOIN orders o
            ON c.customer_id = o.customer_id
        JOIN order_items oi
            ON o.order_id = oi.order_id
        GROUP BY c.city
        ORDER BY revenue DESC
    """)
    fig4 = px.bar(
        city,
        x="city",
        y="revenue",
    )

    st.plotly_chart(fig4, use_container_width=True)

except mysql.connector.Error as e:
    st.error(f"MySQL Connection Error: {e}")

except Exception as e:
    st.error(f"Application Error: {e}")
