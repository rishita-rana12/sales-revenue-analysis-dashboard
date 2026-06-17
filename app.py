import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Sales & Revenue Analysis Dashboard")
st.markdown("### Interactive Business Intelligence Dashboard")
st.write("Analyze sales performance, revenue trends, and top-performing products.")

# Load Data
df = pd.read_csv("sales_data.csv")

# KPIs
total_revenue = df["Revenue"].sum()
total_quantity = df["Quantity"].sum()
total_products = df["Product"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("Units Sold", total_quantity)
col3.metric("Products", total_products)

# Revenue by Product
st.subheader("Revenue by Product")

product_sales = df.groupby("Product")["Revenue"].sum().reset_index()

fig = px.bar(
    product_sales,
    x="Product",
    y="Revenue"
)

st.plotly_chart(fig)

# Revenue Trend
st.subheader("Revenue Trend")

df["Date"] = pd.to_datetime(df["Date"])

trend = df.groupby("Date")["Revenue"].sum().reset_index()

fig2 = px.line(
    trend,
    x="Date",
    y="Revenue"
)

st.plotly_chart(fig2)

# Category Performance
st.subheader("Category Performance")

category = df.groupby("Category")["Revenue"].sum().reset_index()

fig3 = px.pie(
    category,
    names="Category",
    values="Revenue"
)

st.plotly_chart(fig3)